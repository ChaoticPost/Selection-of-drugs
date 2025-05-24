import React from 'react';
import { Link } from 'react-router-dom';

const Layout: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  return (
    <div className="min-h-screen flex flex-col bg-gray-50">
      <header className="bg-white shadow-sm">
        <div className="container mx-auto px-4 py-4">
          <nav className="flex justify-between items-center">
            <Link to="/" className="text-xl font-bold text-blue-600">MedRec</Link>
            <div className="flex space-x-6">
              <Link to="/" className="text-gray-600 hover:text-blue-600">Главная</Link>
              <Link to="/symptoms" className="text-gray-600 hover:text-blue-600">Симптомы</Link>
              <Link to="/analytics" className="text-gray-600 hover:text-blue-600">Аналитика</Link>
            </div>
          </nav>
        </div>
      </header>
      
      <main className="flex-grow">
        {children}
      </main>
      
      <footer className="bg-gray-800 text-white py-8">
        <div className="container mx-auto px-4">
          <div className="flex flex-col md:flex-row justify-between">
            <div className="mb-6 md:mb-0">
              <h3 className="text-lg font-semibold mb-2">О проекте</h3>
              <p className="text-gray-300 max-w-md">
                Рекомендательная система для подбора лекарств на основе симптомов.
                Разработано в рамках ВКР по цифровой кафедре "Разработка и тестирование сервисов искусственного интеллекта".
              </p>
            </div>
            
            <div>
              <h3 className="text-lg font-semibold mb-2">Важная информация</h3>
              <p className="text-gray-300 max-w-md">
                Данная система не заменяет консультацию врача и предназначена только для информационных целей.
                Перед применением любых лекарств проконсультируйтесь с врачом.
              </p>
            </div>
          </div>
          
          <div className="mt-8 pt-8 border-t border-gray-700 text-center text-gray-400">
            <p>&copy; {new Date().getFullYear()} MedRec. Все права защищены.</p>
          </div>
        </div>
      </footer>
    </div>
  );
};

export default Layout;
