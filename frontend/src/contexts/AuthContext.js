import { createContext, useState } from "react";

// Create a provider component
export const AuthProvider = ({ children }) => {
  const [auth, setAuth] = useState({ token: null });

  return (
    <AuthContext.Provider value={{ auth, setAuth }}>
      {children}
    </AuthContext.Provider>
  );
};

// Create a context
export const AuthContext = createContext();
