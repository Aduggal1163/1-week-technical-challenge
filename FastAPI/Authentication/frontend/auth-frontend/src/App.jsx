import { useState, useEffect } from "react";
import axios from "axios";

function App() {
  const [page, setPage] = useState("login"); // login | signup | dashboard
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [user, setUser] = useState(null);

  const API = axios.create({
    baseURL: "http://localhost:8000",
  });

  // Attach token automatically
  API.interceptors.request.use((req) => {
    const token = localStorage.getItem("token");
    if (token) {
      req.headers.Authorization = `Bearer ${token}`;
    }
    return req;
  });

  // ===============================
  // CHECK IF USER ALREADY LOGGED IN
  // ===============================
  useEffect(() => {
    const token = localStorage.getItem("token");
    if (token) {
      fetchUser();
    }
  }, []);

  const fetchUser = async () => {
    try {
      const res = await API.get("/me");
      setUser(res.data);
      setPage("dashboard");
    } catch (err) {
      localStorage.removeItem("token");
      setPage("login");
    }
  };

  // ===============================
  // SIGNUP
  // ===============================
  const handleSignup = async (e) => {
    e.preventDefault();

    try {
      await API.post("/signup", {
        username,
        password,
      });

      alert("Signup successful!");
      setPage("login");
    } catch (err) {
      alert(err.response?.data?.detail || "Signup failed");
    }
  };

  // ===============================
  // LOGIN
  // ===============================
  const handleLogin = async (e) => {
    e.preventDefault();

    const formData = new URLSearchParams();
    formData.append("username", username);
    formData.append("password", password);

    try {
      const res = await API.post("/login", formData, {
        headers: {
          "Content-Type": "application/x-www-form-urlencoded",
        },
      });

      localStorage.setItem("token", res.data.access_token);
      fetchUser();
    } catch (err) {
      alert("Invalid credentials");
    }
  };

  // ===============================
  // LOGOUT
  // ===============================
  const logout = () => {
    localStorage.removeItem("token");
    setUser(null);
    setPage("login");
  };

  // ===============================
  // UI
  // ===============================

  if (page === "signup") {
    return (
      <div style={{ padding: 30 }}>
        <h2>Signup</h2>

        <form onSubmit={handleSignup}>
          <input
            type="text"
            placeholder="Username"
            required
            onChange={(e) => setUsername(e.target.value)}
          />
          <br /><br />

          <input
            type="password"
            placeholder="Password"
            required
            onChange={(e) => setPassword(e.target.value)}
          />
          <br /><br />

          <button type="submit">Signup</button>
        </form>

        <br />
        <button onClick={() => setPage("login")}>
          Already have account? Login
        </button>
      </div>
    );
  }

  if (page === "dashboard") {
    return (
      <div style={{ padding: 30 }}>
        <h2>Dashboard</h2>

        {user && (
          <>
            <p><strong>ID:</strong> {user.id}</p>
            <p><strong>Username:</strong> {user.username}</p>
          </>
        )}

        <br />
        <button onClick={logout}>Logout</button>
      </div>
    );
  }

  // Default → Login Page
  return (
    <div style={{ padding: 30 }}>
      <h2>Login</h2>

      <form onSubmit={handleLogin}>
        <input
          type="text"
          placeholder="Username"
          required
          onChange={(e) => setUsername(e.target.value)}
        />
        <br /><br />

        <input
          type="password"
          placeholder="Password"
          required
          onChange={(e) => setPassword(e.target.value)}
        />
        <br /><br />

        <button type="submit">Login</button>
      </form>

      <br />
      <button onClick={() => setPage("signup")}>
        Create new account
      </button>
    </div>
  );
}

export default App;