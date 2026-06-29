import { BrowserRouter, Routes, Route } from "react-router-dom";

import Dashboard from "./pages/Dashboard";
import UploadRepo from "./pages/UploadRepo";
import Status from "./pages/Status";
import Chat from "./pages/Chat";
import Guide from "./pages/Guide";
import KnowledgeGraph from "./pages/KnowledgeGraph";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Dashboard />} />
        <Route path="/upload" element={<UploadRepo />} />
        <Route path="/status" element={<Status />} />
        <Route path="/chat" element={<Chat />} />
        <Route path="/guide" element={<Guide />} />
        <Route
          path="/knowledge-graph"
          element={<KnowledgeGraph />}
        />
      </Routes>
    </BrowserRouter>
  );
}

export default App;