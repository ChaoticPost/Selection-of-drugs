import React from 'react';
import { Link } from 'react-router-dom';
import Layout from '../components/layout/Layout';
import { useAppContext } from '../context/AppContext';

const ResultsPage: React.FC = () => {
  const { results, selectedSymptoms } = useAppContext();
  
  if (!results) {
    return (
      <Layout>
        <div className="container mx-auto px-4 py-8">
          <div className="max-w-4xl mx-auto text-center">
            <h1 className="text-3xl font-bold text-gray-900 mb-6">Результаты не найдены</h1>
            <p className="text-gray-600 mb-6">
              Пожалуйста, вернитесь на страницу ввода симптомов и выберите симптомы для получения рекомендаций.
            </p>
            <Link
              to="/symptoms"
              className="inline-block bg-blue-600 hover:bg-blue-700 text-white font-bold py-2 px-6 rounded-md"
            >
              Вернуться к вводу симптомов
            </Link>
          </div>
        </div>
      </Layout>
    );
  }
  
  return (
    <Layout>
      <div className="container mx-auto px-4 py-8">
        <div className="max-w-4xl mx-auto">
          <h1 className="text-3xl font-bold text-gray-900 mb-6">Результаты анализа</h1>
          
          <div className="bg-white rounded-lg shadow-lg p-6 mb-8">
            <h2 className="text-xl font-semibold text-gray-800 mb-4">Указанные симптомы</h2>
            <ul className="list-disc list-inside text-gray-600 mb-6 pl-4">
              {selectedSymptoms.map(symptom => (
                <li key={symptom.id}>{symptom.name}</li>
              ))}
            </ul>
            
            <div className="border-t border-gray-200 pt-6 mb-6">
              <h2 className="text-xl font-semibold text-gray-800 mb-4">Предполагаемое заболевание</h2>
              <div className="bg-blue-50 p-4 rounded-md mb-4">
                <h3 className="text-lg font-medium text-blue-800 mb-2">{results.disease.name}</h3>
                <p className="text-gray-600">{results.disease.description}</p>
              </div>
              <div className="bg-yellow-50 border-l-4 border-yellow-400 p-4">
                <p className="text-yellow-700">
                  <strong>Важно:</strong> Это предварительный анализ на основе указанных симптомов. 
                  Для точного диагноза обратитесь к врачу.
                </p>
              </div>
            </div>
            
            <div className="border-t border-gray-200 pt-6">
              <h2 className="text-xl font-semibold text-gray-800 mb-4">Рекомендуемые лекарства</h2>
              <div className="space-y-6">
                {results.medications.map(medication => (
                  <div key={medication.id} className="bg-gray-50 p-4 rounded-md">
                    <h3 className="text-lg font-medium text-gray-800 mb-2">{medication.name}</h3>
                    <p className="text-gray-600 mb-3">{medication.description}</p>
                    
                    <div className="mb-3">
                      <h4 className="text-sm font-semibold text-gray-700 mb-1">Дозировка:</h4>
                      <p className="text-gray-600">{medication.dosage}</p>
                    </div>
                    
                    <div className="mb-3">
                      <h4 className="text-sm font-semibold text-gray-700 mb-1">Побочные эффекты:</h4>
                      <ul className="list-disc list-inside text-gray-600 pl-4">
                        {medication.sideEffects.map((effect, index) => (
                          <li key={index}>{effect}</li>
                        ))}
                      </ul>
                    </div>
                    
                    <div>
                      <h4 className="text-sm font-semibold text-gray-700 mb-1">Эффективность:</h4>
                      <div className="w-full bg-gray-200 rounded-full h-2.5">
                        <div 
                          className="bg-blue-600 h-2.5 rounded-full" 
                          style={{ width: `${medication.effectiveness * 100}%` }}
                        ></div>
                      </div>
                      <p className="text-right text-sm text-gray-500 mt-1">
                        {Math.round(medication.effectiveness * 100)}%
                      </p>
                    </div>
                  </div>
                ))}
              </div>
            </div>
          </div>
          
          <div className="flex justify-between">
            <Link
              to="/symptoms"
              className="bg-gray-200 hover:bg-gray-300 text-gray-800 font-medium py-2 px-6 rounded-md"
            >
              Изменить симптомы
            </Link>
            
            <Link
              to="/analytics"
              className="bg-blue-600 hover:bg-blue-700 text-white font-bold py-2 px-6 rounded-md"
            >
              Перейти к аналитике
            </Link>
          </div>
        </div>
      </div>
    </Layout>
  );
};

export default ResultsPage;
