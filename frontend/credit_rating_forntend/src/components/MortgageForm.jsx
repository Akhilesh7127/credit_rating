// components/MortgageForm.jsx
import React, { useState, useEffect } from 'react';

const MortgageForm = ({ onSubmit, editingMortgage, onCancel }) => {
  const [form, setForm] = useState({
    credit_score: '',
    loan_amount: '',
    property_value: '',
    annual_income: '',
    debt_amount: '',
    loan_type: 'fixed',
    property_type: 'single_family',
  });

  useEffect(() => {
    if (editingMortgage) {
      setForm(editingMortgage);
    }
  }, [editingMortgage]);

  const handleChange = (e) => {
    const { name, value,type } = e.target;
    setForm((prev) => ({ ...prev, [name]: type === 'number' ? Number(value) : value}));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    onSubmit(form);
    setForm({
      credit_score: '',
      loan_amount: '',
      property_value: '',
      annual_income: '',
      debt_amount: '',
      loan_type: 'fixed',
      property_type: 'single_family',
    });
  };

  return (
    <form onSubmit={handleSubmit} className="mb-6 grid grid-cols-2 gap-4 bg-white p-6 rounded shadow">
      <div>
        <label className="block font-medium">Credit Score</label>
        <input
          type="number"
          name="credit_score"
          value={form.credit_score}
          onChange={handleChange}
          min="300"
          max="850"
          className="w-full p-2 border rounded"
          required
        />
      </div>
      <div>
        <label className="block font-medium">Loan Amount</label>
        <input
          type="number"
          name="loan_amount"
          value={form.loan_amount}
          onChange={handleChange}
          className="w-full p-2 border rounded"
          required
        />
      </div>
      <div>
        <label className="block font-medium">Property Value</label>
        <input
          type="number"
          name="property_value"
          value={form.property_value}
          onChange={handleChange}
          className="w-full p-2 border rounded"
          required
        />
      </div>
      <div>
        <label className="block font-medium">Annual Income</label>
        <input
          type="number"
          name="annual_income"
          value={form.annual_income}
          onChange={handleChange}
          className="w-full p-2 border rounded"
          required
        />
      </div>
      <div>
        <label className="block font-medium">Debt Amount</label>
        <input
          type="number"
          name="debt_amount"
          value={form.debt_amount}
          onChange={handleChange}
          className="w-full p-2 border rounded"
          required
        />
      </div>
      <div>
        <label className="block font-medium">Loan Type</label>
        <select
          name="loan_type"
          value={form.loan_type}
          onChange={handleChange}
          className="w-full p-2 border rounded"
        >
          <option value="fixed">Fixed</option>
          <option value="adjustable">Adjustable</option>
        </select>
      </div>
      <div>
        <label className="block font-medium">Property Type</label>
        <select
          name="property_type"
          value={form.property_type}
          onChange={handleChange}
          className="w-full p-2 border rounded"
        >
          <option value="single_family">Single Family</option>
          <option value="condo">Condo</option>
        </select>
      </div>
      <div className="col-span-2 flex justify-end gap-4 mt-4">
        <button
          type="submit"
          className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700"
        >
          {editingMortgage ? 'Update Mortgage' : 'Add Mortgage'}
        </button>
        <button
          type="button"
          onClick={onCancel}
          className="bg-gray-300 px-4 py-2 rounded hover:bg-gray-400"
        >
          Cancel
        </button>
      </div>
    </form>
  );
};

export default MortgageForm;