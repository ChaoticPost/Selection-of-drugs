import React from 'react';
import { Link } from 'react-router-dom';
import { analyticsData } from '../services/mockData';
import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  Legend,
  ResponsiveContainer,
  PieChart,
  Pie,
  Cell
} from 'recharts';
import Layout from '../components/layout/Layout';

const AnalyticsPage: React.FC = () => {
  const { symptomStats, medicationStats, diseaseStats } = analyticsData;
  
  // Цвета для графиков
  const COLORS = ['#0088FE', '#00C49F', '#FFBB28', '#FF8042', '#8884d8', '#82ca9d', '#ffc658', '#8dd1e1', '#a4de6c', '#d0ed57'];

  return (
    <Layout>
      <div className="container mx-auto px-4 py-8">
        <div className="max-w-6xl mx-auto">
          <h1 className="text-3xl font-bold text-gray-900 mb-6">Аналитика и статистика</h1>
          
          <div className="bg-white rounded-lg shadow-lg p-6 mb-8">
            <h2 className="text-xl font-semibold text-gray-800 mb-4">Популярные симптомы</h2>
            <p className="text-gray-600 mb-6">
              Распределение частоты симптомов, указанных пользователями системы.
            </p>
            
            <div className="h-80 w-full">
              <ResponsiveContainer width="100%" height="100%">
                <BarChart
                  data={symptomStats}
                  margin={{ top: 20, right: 30, left: 20, bottom: 70 }}
                >
                  <CartesianGrid strokeDasharray="3 3" />
                  <XAxis 
                    dataKey="symptomName" 
                    angle={-45} 
                    textAnchor="end" 
                    height={70} 
                    tick={{ fontSize: 12 }}
                  />
                  <YAxis />
                  <Tooltip />
                  <Legend />
                  <Bar dataKey="count" name="Количество" fill="#0088FE" />
                </BarChart>
              </ResponsiveContainer>
            </div>
          </div>
          
          <div className="grid md:grid-cols-2 gap-8 mb-8">
            <div className="bg-white rounded-lg shadow-lg p-6">
              <h2 className="text-xl font-semibold text-gray-800 mb-4">Эффективность лекарств</h2>
              <p className="text-gray-600 mb-6">
                Сравнение эффективности наиболее часто рекомендуемых лекарств.
              </p>
              
              <div className="h-80 w-full">
                <ResponsiveContainer width="100%" height="100%">
                  <BarChart
                    data={medicationStats.slice(0, 5)}
                    margin={{ top: 20, right: 30, left: 20, bottom: 50 }}
                  >
                    <CartesianGrid strokeDasharray="3 3" />
                    <XAxis 
                      dataKey="medicationName" 
                      angle={-45} 
                      textAnchor="end" 
                      height={50} 
                      tick={{ fontSize: 12 }}
                    />
                    <YAxis domain={[0, 1]} tickFormatter={(value) => `${Math.round(value * 100)}%`} />
                    <Tooltip formatter={(value) => `${Math.round(value * 100)}%`} />
                    <Legend />
                    <Bar dataKey="effectiveness" name="Эффективность" fill="#00C49F" />
                  </BarChart>
                </ResponsiveContainer>
              </div>
            </div>
            
            <div className="bg-white rounded-lg shadow-lg p-6">
              <h2 className="text-xl font-semibold text-gray-800 mb-4">Распределение заболеваний</h2>
              <p className="text-gray-600 mb-6">
                Распределение заболеваний по средней эффективности лекарств.
              </p>
              
              <div className="h-80 w-full">
                <ResponsiveContainer width="100%" height="100%">
                  <PieChart>
                    <Pie
                      data={diseaseStats}
                      cx="50%"
                      cy="50%"
                      labelLine={true}
                      outerRadius={80}
                      fill="#8884d8"
                      dataKey="averageEffectiveness"
                      nameKey="diseaseName"
                      label={({ name, percent }) => `${name}: ${(percent * 100).toFixed(0)}%`}
                    >
                      {diseaseStats.map((entry, index) => (
                        <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
                      ))}
                    </Pie>
                    <Tooltip formatter={(value) => `${Math.round(value * 100)}%`} />
                    <Legend />
                  </PieChart>
                </ResponsiveContainer>
              </div>
            </div>
          </div>
          
          <div className="bg-white rounded-lg shadow-lg p-6 mb-8">
            <h2 className="text-xl font-semibold text-gray-800 mb-4">Количество отзывов по лекарствам</h2>
            <p className="text-gray-600 mb-6">
              Распределение количества отзывов по наиболее популярным лекарствам.
            </p>
            
            <div className="h-80 w-full">
              <ResponsiveContainer width="100%" height="100%">
                <BarChart
                  data={medicationStats}
                  margin={{ top: 20, right: 30, left: 20, bottom: 70 }}
                >
                  <CartesianGrid strokeDasharray="3 3" />
                  <XAxis 
                    dataKey="medicationName" 
                    angle={-45} 
                    textAnchor="end" 
                    height={70} 
                    tick={{ fontSize: 12 }}
                  />
                  <YAxis />
                  <Tooltip />
                  <Legend />
                  <Bar dataKey="reviewCount" name="Количество отзывов" fill="#FFBB28" />
                </BarChart>
              </ResponsiveContainer>
            </div>
          </div>
          
          <div className="flex justify-between">
            <Link
              to="/results"
              className="bg-gray-200 hover:bg-gray-300 text-gray-800 font-medium py-2 px-6 rounded-md"
            >
              Вернуться к результатам
            </Link>
            
            <Link
              to="/"
              className="bg-blue-600 hover:bg-blue-700 text-white font-bold py-2 px-6 rounded-md"
            >
              На главную
            </Link>
          </div>
        </div>
      </div>
    </Layout>
  );
};

export default AnalyticsPage;
