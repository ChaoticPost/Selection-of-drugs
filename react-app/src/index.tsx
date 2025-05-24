// Типы для симптомов
export interface Symptom {
  id: string;
  name: string;
}

// Типы для заболеваний
export interface Disease {
  id: string;
  name: string;
  description: string;
}

// Типы для лекарств
export interface Medication {
  id: string;
  name: string;
  description: string;
  dosage: string;
  sideEffects: string[];
  effectiveness: number;
}

// Типы для результатов
export interface Result {
  disease: Disease;
  medications: Medication[];
}

// Типы для аналитики
export interface SymptomStat {
  symptomName: string;
  count: number;
}

export interface MedicationStat {
  medicationName: string;
  effectiveness: number;
  reviewCount: number;
}

export interface DiseaseStat {
  diseaseName: string;
  averageEffectiveness: number;
}

export interface AnalyticsData {
  symptomStats: SymptomStat[];
  medicationStats: MedicationStat[];
  diseaseStats: DiseaseStat[];
}
