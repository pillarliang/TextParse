import type { Metadata } from "next";
import "./globals.css";
import Sidebar from "./ui/sidebar";
import UploadFile from "./ui/upload-file.client";

export const metadata: Metadata = {
  title: 'Text Parse',
  description: 'Text Parse for RAG.',
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body>
        <div className="container">
          <div className="main">
            <Sidebar>
              <UploadFile />
            </Sidebar>
            <section className="col note-viewer">{children}</section>
          </div>
        </div>
      </body>
    </html>
  );
}
