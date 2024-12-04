import React, { useState, useEffect } from "react";

let url = "http://localhost:5000";

export default function Chat() {
  const [inputValue, setInputValue] = useState("");
  const [coords, setCoords] = useState(null);
  const [appStarted, setAppStarted] = useState(true);
  const [isLoading, setIsLoading] = useState(false); 

  const sendInputValue = (input) => {
    setCoords(null);
    setIsLoading(true); 
    fetch(`${url}/input`, {
      method: "POST",
      mode: "cors",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ input }),
    })
      .then((response) => response.json())
      .then((data) => {
        setCoords(JSON.stringify(data.coords));
        setIsLoading(false); 
      })
      .catch((error) => {
        console.log(error);
        setIsLoading(false); 
      });
  };

  const handleKeyDown = (event) => {
    if (event.key === "Enter") {
      const currentInput = event.target.value;
      event.target.value = "";
      setInputValue(currentInput);
    }
  };

  useEffect(() => {
    if (inputValue) {
      setAppStarted(false);
      sendInputValue(inputValue);
    } else {
      setCoords("false");
    }
  }, [inputValue]);

  console.log(coords === "false");
  return (
    <div className="min-h-screen bg-blue-500 flex flex-col justify-center items-center p-6 space-y-6">
      <h1 className="text-4xl font-bold text-white mb-4">ParkGPT</h1>
      {appStarted && <div className="text-black text-center p-6 rounded-lg bg-red-400 shadow-lg w-full max-w-xl">
            Alert: Unpaid spots may be occupied
          </div>}
      <div className="flex flex-col items-center w-full max-w-xl space-y-6">
        {isLoading || coords === null ? (
          <div className="bg-white text-black text-center p-6 rounded-lg shadow-lg w-full">
            Loading...
          </div>
        ) : coords === "false" ? (
          <div className="bg-white text-black text-center p-6 rounded-lg shadow-lg w-full">
            {appStarted ? "Enter where you would like to park" : "Please enter a more specific location"}
          </div>
        ) : (
          <iframe
            width="90%"
            height="300"
            frameborder="0"
            style={{ border: "0" }}
            referrerpolicy="no-referrer-when-downgrade"
            allowFullScreen
            className="rounded-lg shadow-lg mb-8 w-full"
          ></iframe>
        )}

        {coords !== "false" && inputValue && (
          <div className="bg-white text-black p-6 rounded-lg shadow-lg w-full mb-8">
            <h2 className="text-xl font-bold">Location:</h2>
            {inputValue}
          </div>
        )}

        <input
          type="text"
          onKeyDown={handleKeyDown}
          className="p-4 border-2 border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-600 w-full text-lg"
          placeholder="Enter your text here"
        />
      </div>
    </div>
  );
}
