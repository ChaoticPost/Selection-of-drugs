import React from 'react';
import { Link } from 'react-router-dom';
import Layout from '../components/layout/Layout';

const HomePage: React.FC = () => {
  return (
    <Layout>
      <div className="container mx-auto px-4 py-12">
        <div className="max-w-4xl mx-auto">
          <div className="text-center mb-12">
            <h1 className="text-4xl font-bold text-gray-900 mb-4">Рекомендательная система для подбора лекарств</h1>
            <p className="text-xl text-gray-600">
              Получите персонализированные рекомендации по лекарствам на основе ваших симптомов
            </p>
          </div>
          
          <div className="bg-white rounded-lg shadow-lg overflow-hidden mb-12">
            <div className="p-8">
              <h2 className="text-2xl font-semibold text-gray-800 mb-4">О проекте</h2>
              <p className="text-gray-600 mb-6">
                Наша система использует методы машинного обучения для анализа связей между симптомами, 
                заболеваниями и эффективностью различных лекарств. На основе этого анализа мы предоставляем 
                персонализированные рекомендации, которые помогут вам получить информацию о возможных 
                лекарствах для облегчения ваших симптомов.
              </p>
              
              <h3 className="text-xl font-semibold text-gray-800 mb-3">Как это работает:</h3>
              <ol className="list-decimal list-inside text-gray-600 mb-6 pl-4">
                <li className="mb-2">Выберите симптомы, которые вас беспокоят</li>
                <li className="mb-2">Наша система проанализирует ваши симптомы</li>
                <li className="mb-2">Вы получите информацию о возможном заболевании</li>
                <li>Мы предложим список рекомендуемых лекарств с подробной информацией</li>
              </ol>
              
              <div className="bg-yellow-50 border-l-4 border-yellow-400 p-4 mb-6">
                <p className="text-yellow-700">
                  <strong>Важно:</strong> Данная система не заменяет консультацию врача и предназначена 
                  только для информационных целей. Перед применением любых лекарств проконсультируйтесь с врачом.
                </p>
              </div>
              
              <div className="text-center">
                <Link
                  to="/symptoms"
                  className="inline-block bg-blue-600 hover:bg-blue-700 text-white font-bold py-3 px-8 rounded-md transition duration-300"
                >
                  Начать
                </Link>
              </div>
            </div>
          </div>
          
          <div className="grid md:grid-cols-3 gap-8">
            <div className="bg-white rounded-lg shadow-md p-6">
              <h3 className="text-xl font-semibold text-gray-800 mb-3">Точность</h3>
              <p className="text-gray-600">
                Наша система обучена на большом количестве данных о симптомах, заболеваниях и лекарствах, 
                что обеспечивает высокую точность рекомендаций.
              </p>
            </div>
            
            <div className="bg-white rounded-lg shadow-md p-6">
              <h3 className="text-xl font-semibold text-gray-800 mb-3">Удобство</h3>
              <p className="text-gray-600">
                Простой и интуитивно понятный интерфейс позволяет быстро получить рекомендации 
                по лекарствам без необходимости изучения медицинской литературы.
              </p>
            </div>
            
            <div className="bg-white rounded-lg shadow-md p-6">
              <h3 className="text-xl font-semibold text-gray-800 mb-3">Информативность</h3>
              <p className="text-gray-600">
                Для каждого рекомендуемого лекарства предоставляется подробная информация о дозировке, 
                применении и возможных побочных эффектах.
              </p>
            </div>
          </div>
        </div>
      </div>
    </Layout>
  );
};

export default HomePage;
