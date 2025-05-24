import React, { createContext, useState, useContext, ReactNode } from 'react';
import { Symptom, Result } from '../types';
import { symptoms, getResultsBySymptoms } from '../services/mockData';

interface AppContextType {
  availableSymptoms: Symptom[];
  selectedSymptoms: Symptom[];
  results: Result | null;
  addSymptom: (symptom: Symptom) => void;
  removeSymptom: (symptomId: string) => void;
  getResults: () => void;
  resetResults: () => void;
}

const AppContext = createContext<AppContextType | undefined>(undefined);

export const AppProvider: React.FC<{ children: ReactNode }> = ({ children }) => {
  const [selectedSymptoms, setSelectedSymptoms] = useState<Symptom[]>([]);
  const [results, setResults] = useState<Result | null>(null);

  const addSymptom = (symptom: Symptom) => {
    if (!selectedSymptoms.some(s => s.id === symptom.id)) {
      setSelectedSymptoms([...selectedSymptoms, symptom]);
    }
  };

  const removeSymptom = (symptomId: string) => {
    setSelectedSymptoms(selectedSymptoms.filter(s => s.id !== symptomId));
  };

  const getResults = () => {
    if (selectedSymptoms.length > 0) {
      const selectedSymptomIds = selectedSymptoms.map(s => s.id);
      const results = getResultsBySymptoms(selectedSymptomIds);
      setResults(results);
    }
  };

  const resetResults = () => {
    setResults(null);
    setSelectedSymptoms([]);
  };

  return (
    <AppContext.Provider
      value={{
        availableSymptoms: symptoms,
        selectedSymptoms,
        results,
        addSymptom,
        removeSymptom,
        getResults,
        resetResults
      }}
    >
      {children}
    </AppContext.Provider>
  );
};

export const useAppContext = () => {
  const context = useContext(AppContext);
  if (context === undefined) {
    throw new Error('useAppContext must be used within an AppProvider');
  }
  return context;
};
