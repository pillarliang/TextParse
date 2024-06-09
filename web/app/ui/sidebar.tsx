'use client'

import React, { Suspense } from 'react'
import Link from 'next/link'
import Image from 'next/image' // Import the 'Image' component from 'next/image'

export default function Sidebar({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <>
      <input type="checkbox" className="sidebar-toggle" id="sidebar-toggle" />
      <section className="col sidebar">
        <Link href={'/'} className="link--unstyled">
          <section className="sidebar-header">
            <Image
              className="logo"
              src="/logo.png"
              width={18}
              height={22}
              alt=""
              role="presentation"
            />
            <strong>Text Parse</strong>
          </section>
        </Link>
        {/* upload file */}
        <section className="sidebar-menu" role="menubar">
          {children}
        </section>
      </section>
    </>
  )
}
