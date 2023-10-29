import React, { useState } from 'react';

function App() {
  const [selectedTemplate, setSelectedTemplate] = useState('Rental Agreement');
  const [userInput, setUserInput] = useState({});
  const [generatedDocument, setGeneratedDocument] = useState('');
  const [editing, setEditing] = useState(false);
  const [editedDocument, setEditedDocument] = useState('');

  const legalDocumentTemplates = {
    "Rental Agreement": "Generate a legal contract for a rental agreement between {landlord_name} and {tenant_name} for the property located at {property_address}. The agreement should include the following terms and conditions:\n\n1. Agreement Date: {agreement_date}\n2. Rent Amount: ${rent_amount} per month\n3. Lease Term: {lease_term} months\n4. Security Deposit: ${security_deposit}",
    "Rental Agreemen": "Generate a legal contract for a rental agreement between {landlord_name} and {tenant_name} for the property located at {property_address}. The agreement should include the following terms and conditions:\n\n1. Agreement Date: {agreement_date}\n2. Rent Amount: ${rent_amount} per month\n3. Lease Term: {lease_term} months\n4. Security Deposit: ${security_deposit}",
    "Renal Agreement": "Generate a legal contract for a rental agreement between {landlord_name} and {tenant_name} for the property located at {property_address}. The agreement should include the following terms and conditions:\n\n1. Agreement Date: {agreement_date}\n2. Rent Amount: ${rent_amount} per month\n3. Lease Term: {lease_term} months\n4. Security Deposit: ${security_deposit}",

    // Add other templates here
  };

  const resetInputFields = () => {
    setUserInput({});
  };

  const generateDocument = () => {
    const template = legalDocumentTemplates[selectedTemplate];
    // Implement your document generation logic here
    // Replace this with a call to your OpenAI API or any other backend logic
    const generatedDoc = `Generated document content for template: ${selectedTemplate}`;
    setGeneratedDocument(generatedDoc);
    setEditing(true);
  };

  const saveAsPDF = () => {
    // Implement your logic to save the document as PDF
    // You can use libraries like jsPDF for PDF generation
  };

  // Helper function to render input fields based on the selected template
  const renderInputFields = () => {
    if (selectedTemplate === 'Rental Agreement') {
      return (
        <div>
          <label className="block text-lg font-medium mb-2">Landlord Name</label>
          <input
            type="text"
            className="w-full p-2 border rounded-md mb-4"
            value={userInput.landlord_name || ''}
            onChange={(e) => setUserInput({ ...userInput, landlord_name: e.target.value })}
          />
          {/* Add more input fields for Rental Agreement parameters */}
        </div>
      );
    } else if (selectedTemplate === 'Divorce Agreement') {
      return (
        <div>
          <label className="block text-lg font-medium mb-2">Husband Name</label>
          <input
            type="text"
            className="w-full p-2 border rounded-md mb-4"
            value={userInput.husband_name || ''}
            onChange={(e) => setUserInput({ ...userInput, husband_name: e.target.value })}
          />
          {/* Add more input fields for Divorce Agreement parameters */}
        </div>
      );
    }
    // Add other template cases here
  };

  return (
    <div className="bg-gray-100 min-h-screen sm:flex items-center">
      <div className="sm:w-1/8">
        <img src="logo.png" alt="Logo" className="w-24 h-24 mx-auto mb-4" />
        <img src="legdoc.jpg" alt="Legal Document" className="w-full" />
      </div>
      <div className="sm:w-2/3 p-4 bg-white rounded-lg shadow-lg m-3 mr-10 w-9">
        <h1 className="text-3xl font-semibold mb-4">Legal Document Generator and Editor</h1>
        <div className="mb-6">
          <label className="block text-lg font-medium mb-2">Select a Legal Document Template</label>
          <select
            value={selectedTemplate}
            onChange={(e) => setSelectedTemplate(e.target.value)}
            className="w-full p-2 border rounded-md">
            {Object.keys(legalDocumentTemplates).map((template) => (
              <option key={template} value={template}>{template}</option>
            ))}
          </select>
        </div>
        {renderInputFields()} {/* Render input fields based on the selected template */}
        <div className="mb-6">
          <button className="bg-blue-500 text-white py-2 px-4 rounded-md" onClick={generateDocument}>Generate Document</button>
          <button className="bg-red-500 text-white py-2 px-4 rounded-md ml-2" onClick={resetInputFields}>Reset Input Fields</button>
        </div>
        <div id="generatedDocument" className="prose bg-gray-200 p-4 rounded-md mb-4">
          {editing ? (
            <textarea
              id="editDocument"
              className="w-full p-4 border rounded-md"
              rows="10"
              placeholder="Edit the generated document"
              value={editedDocument}
              onChange={(e) => setEditedDocument(e.target.value)}
            />
          ) : (
            generatedDocument
          )}
        </div>
        {editing && (
          <button className="bg-green-500 text-white py-2 px-4 rounded-md" onClick={saveAsPDF}>Save as PDF</button>
        )}
        <p className="text-sm text-gray-600 mt-4">Disclaimer: The generated document should be reviewed by a legal professional for accuracy and compliance with local laws and regulations.</p>
      </div>
    </div>
  );
}

export default App;
