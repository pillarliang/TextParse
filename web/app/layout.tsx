import type { Metadata } from "next";
import { Inter } from "next/font/google";
import "./globals.css";
import Sidebar from "./ui/sidebar";
import UploadFile from "./ui/upload-file.client";

const inter = Inter({ subsets: ["latin"] });

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
      <body className={inter.className}>
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
