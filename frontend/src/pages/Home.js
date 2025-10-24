import React, {useEffect, useState} from 'react';
export default function Home(){
  return (
    <div>
      <h2>Landing</h2>
      <p>This page should display two landing charts: matches per year and stacked wins per season.</p>
      <p>Use the backend API endpoints to fetch data and plot charts (see README in backend/).</p>
    </div>
  );
}