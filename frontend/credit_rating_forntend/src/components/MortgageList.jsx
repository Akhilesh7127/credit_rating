import React from 'react';

const MortgageList = ({ mortgages, onEdit, onDelete, onView }) => {
  return (
    <table className="w-full border border-collapse shadow">
      <thead>
        <tr className="bg-gray-200 text-left">
          <th className="border p-2">Credit Score</th>
          <th className="border p-2">Loan</th>
          <th className="border p-2">Property</th>
          <th className="border p-2">Income</th>
          <th className="border p-2">Debt</th>
          <th className="border p-2">Loan Type</th>
          <th className="border p-2">Property Type</th>
          <th className="border p-2">Rating</th>
          <th className="border p-2">Actions</th>
        </tr>
      </thead>
      <tbody>
        {mortgages.map((m) => (
          <tr key={m.id} className="hover:bg-gray-50">
            <td className="border p-2">{m.credit_score}</td>
            <td className="border p-2">{m.loan_amount.toLocaleString()}</td>
            <td className="border p-2">{m.property_value.toLocaleString()}</td>
            <td className="border p-2">{m.annual_income.toLocaleString()}</td>
            <td className="border p-2">{m.debt_amount.toLocaleString()}</td>
            <td className="border p-2">{m.loan_type}</td>
            <td className="border p-2">{m.property_type}</td>
            <td className="border p-2 font-bold">{m.credit_rating}</td>
            <td className="border p-2 space-x-2">
              <button onClick={() => onEdit(m)} className="text-blue-500 hover:underline">Edit</button>
              <button onClick={() => onView(m)} className="text-green-600 hover:underline">View</button>
              <button onClick={() => onDelete(m.id)} className="text-red-500 hover:underline">Delete</button>
            </td>
          </tr>
        ))}
      </tbody>
    </table>
  );
};

export default MortgageList;
