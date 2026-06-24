import {
  LayoutDashboard,
  Upload,
  Activity,
  MessageSquare,
  BrainCircuit
} from "lucide-react";

import { NavLink } from "react-router-dom";

function Sidebar() {

  const linkClass = ({ isActive }) =>
    `flex items-center gap-3 px-4 py-3 rounded-xl transition-all duration-300 ${
      isActive
        ? "bg-[#8b5e3c] text-white shadow-lg"
        : "text-[#b8a08d] hover:bg-[#2d2118] hover:text-white"
    }`;

  return (
    <div
      className="
        w-72
        min-h-screen
        bg-[#1c140d]/90
        backdrop-blur-xl
        border-r
        border-[#3a2b20]
        p-6
        shadow-2xl
      "
    >

      <div className="flex items-center gap-4 mb-12">

        <div className="bg-[#c68b59] p-3 rounded-xl shadow-lg">
          <BrainCircuit size={24} />
        </div>

        <div>
          <h1 className="text-2xl font-bold text-[#f5e6d3]">
            EEIP
          </h1>

          <p className="text-[#b8a08d] text-sm">
            AI Repository Intelligence
          </p>
        </div>

      </div>

      <div className="space-y-3">

        <NavLink
          to="/"
          className={linkClass}
        >
          <LayoutDashboard size={20} />
          Dashboard
        </NavLink>

        <NavLink
          to="/upload"
          className={linkClass}
        >
          <Upload size={20} />
          Upload Repository
        </NavLink>

        <NavLink
          to="/status"
          className={linkClass}
        >
          <Activity size={20} />
          Repository Status
        </NavLink>

        <NavLink
          to="/chat"
          className={linkClass}
        >
          <MessageSquare size={20} />
          Chat Assistant
        </NavLink>

      </div>

    </div>
  );
}

export default Sidebar;