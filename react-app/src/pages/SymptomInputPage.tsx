import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import Layout from '../components/layout/Layout';
import { useAppContext } from '../context/AppContext';
import { Symptom } from '../types';

const SymptomInputPage: React.FC = () => {
  const navigate = useNavigate();
  const { availableSymptoms, selectedSymptoms, addSymptom, removeSymptom, getResults } = useAppContext();
  const [searchTerm, setSearchTerm] = useState('');
  
  const filteredSymptoms = availableSymptoms.filter(
    symptom => symptom.name.toLowerCase().includes(searchTerm.toLowerCase())
  );
  
  const handleAddSymptom = (symptom: Symptom) => {
    addSymptom(symptom);
    setSearchTerm('');
  };
  
  const handleRemoveSymptom = (symptomId: string) => {
    removeSymptom(symptomId);
  };
  
  const handleGetResults = () => {
    getResults();
    navigate('/results');
  };
  
  return (
    <Layout>
      <div className="container mx-auto px-4 py-8">
        <div className="max-w-4xl mx-auto">
          <h1 className="text-3xl font-bold text-gray-900 mb-6">Укажите ваши симптомы</h1>
          
          <div className="bg-white rounded-lg shadow-lg p-6 mb-8">
            <div className="mb-6">
              <label htmlFor="symptom-search" className="block text-gray-700 font-medium mb-2">
                Поиск симптомов
              </label>
              <div className="relative">
                <input
                  id="symptom-search"
                  type="text"
                  className="w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                  placeholder="Введите симптом..."
                  value={searchTerm}
                  onChange={(e) => setSearchTerm(e.target.value)}
                />
              </div>
            </div>
            
            {searchTerm && (
              <div className="mb-6">
                <h3 className="text-lg font-semibold text-gray-800 mb-3">Результаты поиска</h3>
                {filteredSymptoms.length > 0 ? (
                  <ul className="space-y-2">
                    {filteredSymptoms.map(symptom => (
                      <li key={symptom.id} className="flex items-center justify-between p-3 bg-gray-50 rounded-md">
                        <span>{symptom.name}</span>
                        <button
                          className="px-3 py-1 bg-blue-600 text-white rounded-md hover:bg-blue-700"
                          onClick={() => handleAddSymptom(symptom)}
                        >
                          Добавить
                        </button>
                      </li>
                    ))}
                  </ul>
                ) : (
                  <p className="text-gray-600">Симптомы не найдены</p>
                )}
              </div>
            )}
            
            <div>
              <h3 className="text-lg font-semibold text-gray-800 mb-3">Выбранные симптомы</h3>
              {selectedSymptoms.length > 0 ? (
                <ul className="space-y-2 mb-6">
                  {selectedSymptoms.map(symptom => (
                    <li key={symptom.id} className="flex items-center justify-between p-3 bg-blue-50 rounded-md">
                      <span>{symptom.name}</span>
                      <button
                        className="px-3 py-1 bg-red-500 text-white rounded-md hover:bg-red-600"
                        onClick={() => handleRemoveSymptom(symptom.id)}
                      >
                        Удалить
                      </button>
                    </li>
                  ))}
                </ul>
              ) : (
                <p className="text-gray-600 mb-6">Вы еще не выбрали ни одного симптома</p>
              )}
              
              <div className="flex justify-end">
                <button
                  className="px-6 py-2 bg-blue-600 text-white rounded-md hover:bg-blue-700 disabled:bg-gray-400 disabled:cursor-not-allowed"
                  onClick={handleGetResults}
                  disabled={selectedSymptoms.length === 0}
                >
                  Получить рекомендации
                </button>
              </div>
            </div>
          </div>
          
          <div className="bg-yellow-50 border-l-4 border-yellow-400 p-4">
            <p className="text-yellow-700">
              <strong>Примечание:</strong> Чем больше симптомов вы укажете, тем точнее будут рекомендации.
              Однако помните, что данная система не заменяет консультацию врача.
            </p>
          </div>
        </div>
      </div>
    </Layout>
  );
};

export default SymptomInputPage;
