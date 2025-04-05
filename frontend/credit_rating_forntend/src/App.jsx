import React, { useEffect, useState } from 'react';
import MortgageForm from './components/MortgageForm';
import MortgageList from './components/MortgageList';
import ViewModal from './components/ViewModal';
import toast from 'react-hot-toast';

const App = () => {
  const [mortgages, setMortgages] = useState([]);
  const [editingMortgage, setEditingMortgage] = useState(null);
  const [viewingMortgage, setViewingMortgage] = useState(null);
  const [showForm, setShowForm] = useState(false);
  const [showOnlyCreditRating,setShowOnlyCreditRating]=useState(false)

  const API_URL = import.meta.env.VITE_BASE_API_URL;
  const API_KEY = import.meta.env.VITE_API_KEY;
  const ACCOUNT_ID = import.meta.env.VITE_ACCOUNT_ID;

  const headers = {
    'Content-Type': 'application/json',
    'api-key': API_KEY,
    'account-id': ACCOUNT_ID,
  };

  useEffect(() => {
    fetchMortgages();
  },[]);

  const fetchMortgages = async () => {
    const response = await fetch(`${API_URL}/mortgages`, { headers });
    const data = await response.json();
    setMortgages(data);
  };

  const handleSubmit = async (mortgage) => {
    const url = editingMortgage
      ? `${API_URL}/mortgages/${editingMortgage.id}/`
      : `${API_URL}/mortgages/`;
    const method = editingMortgage ? 'PUT' : 'POST';
    try {
      const response = await fetch(url, {
      method,
      headers,
      body: JSON.stringify(mortgage),
    });
    if (!response.ok) {
      throw new Error(data.detail || 'Something went wrong');
    }
    mortgage=await response.json()
    toast.success(editingMortgage ? 'Mortgage updated!' : 'Mortgage added!');
    setEditingMortgage(null);
    setShowForm(false);
    fetchMortgages();
    setShowOnlyCreditRating(true)
    setViewingMortgage(mortgage);
  } catch (error) {
    toast.error(error.message);
  }
  };

  const handleEdit = (mortgage) => {
    setEditingMortgage(mortgage);
    setShowForm(true);
  };

  const handleDelete = async (id) => {
    try{
      const response = await fetch(`${API_URL}/mortgages/${id}`, { method: 'DELETE', headers });
      fetchMortgages();
      if (!response.ok) {
        throw new Error(data.detail || 'Something went wrong');
      }
  
      toast.success('Mortgage deleted!');
    }
    catch (error) {
      toast.error(error.message);
    }
  };

  const handleAddNew = () => {
    setEditingMortgage(null);
    setShowForm(true);
  };

  return (
    <div className="p-6 max-w-6xl mx-auto">
      <h1 className="text-3xl font-bold mb-6 text-center">Mortgage Dashboard</h1>
      <div className="flex justify-end mb-4">
        <button
          onClick={handleAddNew}
          className="bg-green-600 hover:bg-green-700 text-white px-4 py-2 rounded"
        >
          + Add New Mortgage
        </button>
      </div>
      {showForm && (
        <MortgageForm onSubmit={handleSubmit} editingMortgage={editingMortgage} onCancel={() => setShowForm(false)} />
      )}
      <MortgageList
        mortgages={mortgages}
        onEdit={handleEdit}
        onDelete={handleDelete}
        onView={(mortgage) => setViewingMortgage(mortgage)}
      />
      {viewingMortgage && (
        <ViewModal mortgage={viewingMortgage} onClose={() => {setViewingMortgage(null);setShowOnlyCreditRating(null)}} showOnlyCreditRating={showOnlyCreditRating} />
      )}
    </div>
  );
};

export default App;