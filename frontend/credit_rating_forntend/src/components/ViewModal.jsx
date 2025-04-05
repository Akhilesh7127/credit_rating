import React from 'react';

const ViewModal = ({ mortgage, onClose,showOnlyCreditRating }) => {
  console.log(mortgage)
  return (
    <>
      {showOnlyCreditRating ? (
        <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
          <div className="bg-white p-8 rounded-xl shadow-lg text-center max-w-sm w-full">
            <h1 className="text-3xl font-bold text-gray-800 mb-4">Credit Rating</h1>
            <h3 className="text-5xl font-extrabold text-green-600">{mortgage.credit_rating}</h3>
            <div className="mt-6">
              <button
                onClick={onClose}
                className="bg-blue-500 hover:bg-blue-600 text-white px-6 py-2 rounded mt-4"
              >
                Close
              </button>
            </div>
          </div>
        </div>
      ) : (
        <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
          <div className="bg-white p-6 rounded shadow-lg w-full max-w-md">
            <h2 className="text-2xl font-bold mb-4">Mortgage Details</h2>
            <ul className="space-y-2">
              {Object.entries(mortgage).map(([key, value]) => (
                <li key={key}>
                  <strong className="capitalize">{key.replace('_', ' ')}:</strong> {value}
                </li>
              ))}
            </ul>
            <div className="mt-6 text-right">
              <button onClick={onClose} className="bg-blue-500 text-white px-4 py-2 rounded">
                Close
              </button>
            </div>
          </div>
        </div>
      )}
    </>
  );
};
  export default ViewModal;