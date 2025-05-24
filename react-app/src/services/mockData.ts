import { Symptom, Disease, Medication, Result, AnalyticsData } from '../types';

// Мок-данные для симптомов
export const symptoms: Symptom[] = [
  { id: '1', name: 'Головная боль' },
  { id: '2', name: 'Тошнота' },
  { id: '3', name: 'Головокружение' },
  { id: '4', name: 'Повышенная температура' },
  { id: '5', name: 'Боль в горле' },
  { id: '6', name: 'Кашель' },
  { id: '7', name: 'Насморк' },
  { id: '8', name: 'Боль в животе' },
  { id: '9', name: 'Диарея' },
  { id: '10', name: 'Сыпь' },
  { id: '11', name: 'Зуд' },
  { id: '12', name: 'Боль в суставах' },
  { id: '13', name: 'Боль в мышцах' },
  { id: '14', name: 'Усталость' },
  { id: '15', name: 'Бессонница' }
];

// Мок-данные для заболеваний
export const diseases: Disease[] = [
  { 
    id: '1', 
    name: 'Грипп', 
    description: 'Острое респираторное заболевание, вызываемое вирусом гриппа. Характеризуется высокой температурой, ознобом, болью в мышцах и общей слабостью.' 
  },
  { 
    id: '2', 
    name: 'Мигрень', 
    description: 'Неврологическое заболевание, проявляющееся приступами пульсирующей головной боли в одной половине головы. Часто сопровождается тошнотой, рвотой и повышенной чувствительностью к свету и звуку.' 
  },
  { 
    id: '3', 
    name: 'Гастроэнтерит', 
    description: 'Воспаление слизистой оболочки желудка и тонкого кишечника. Обычно вызывается вирусами или бактериями и проявляется диареей, рвотой и болью в животе.' 
  },
  { 
    id: '4', 
    name: 'Аллергический ринит', 
    description: 'Воспаление слизистой оболочки носа, вызванное аллергической реакцией на различные раздражители. Проявляется насморком, чиханием и заложенностью носа.' 
  },
  { 
    id: '5', 
    name: 'Артрит', 
    description: 'Воспаление одного или нескольких суставов. Проявляется болью, отеком и ограничением подвижности суставов.' 
  }
];

// Мок-данные для лекарств
export const medications: Medication[] = [
  { 
    id: '1', 
    name: 'Парацетамол', 
    description: 'Анальгетик и антипиретик, используемый для облегчения боли и снижения температуры.', 
    dosage: 'Взрослым и детям старше 12 лет: 500-1000 мг каждые 4-6 часов, не более 4000 мг в сутки.', 
    sideEffects: ['Аллергические реакции', 'Нарушение функции печени при передозировке'], 
    effectiveness: 0.75 
  },
  { 
    id: '2', 
    name: 'Ибупрофен', 
    description: 'Нестероидный противовоспалительный препарат, используемый для облегчения боли, снижения температуры и уменьшения воспаления.', 
    dosage: 'Взрослым и детям старше 12 лет: 200-400 мг каждые 4-6 часов, не более 1200 мг в сутки.', 
    sideEffects: ['Расстройство желудка', 'Язва желудка', 'Повышенный риск сердечно-сосудистых осложнений'], 
    effectiveness: 0.82 
  },
  { 
    id: '3', 
    name: 'Суматриптан', 
    description: 'Селективный агонист серотониновых рецепторов, используемый для лечения мигрени.', 
    dosage: 'Взрослым: 50-100 мг при появлении симптомов мигрени, при необходимости повторить через 2 часа, не более 300 мг в сутки.', 
    sideEffects: ['Головокружение', 'Сонливость', 'Покалывание в конечностях', 'Тошнота'], 
    effectiveness: 0.88 
  },
  { 
    id: '4', 
    name: 'Лоперамид', 
    description: 'Противодиарейное средство, замедляющее перистальтику кишечника.', 
    dosage: 'Взрослым: начальная доза 4 мг, затем 2 мг после каждого акта дефекации, не более 16 мг в сутки.', 
    sideEffects: ['Запор', 'Вздутие живота', 'Головная боль', 'Сухость во рту'], 
    effectiveness: 0.79 
  },
  { 
    id: '5', 
    name: 'Цетиризин', 
    description: 'Антигистаминный препарат второго поколения, используемый для лечения аллергических реакций.', 
    dosage: 'Взрослым и детям старше 6 лет: 10 мг один раз в сутки.', 
    sideEffects: ['Сонливость', 'Сухость во рту', 'Головная боль'], 
    effectiveness: 0.85 
  },
  { 
    id: '6', 
    name: 'Диклофенак', 
    description: 'Нестероидный противовоспалительный препарат, используемый для лечения боли и воспаления при артрите.', 
    dosage: 'Взрослым: 50 мг 2-3 раза в сутки, не более 150 мг в сутки.', 
    sideEffects: ['Расстройство желудка', 'Язва желудка', 'Повышенный риск сердечно-сосудистых осложнений', 'Повышение артериального давления'], 
    effectiveness: 0.81 
  },
  { 
    id: '7', 
    name: 'Осельтамивир', 
    description: 'Противовирусный препарат, используемый для лечения и профилактики гриппа.', 
    dosage: 'Взрослым: 75 мг два раза в сутки в течение 5 дней.', 
    sideEffects: ['Тошнота', 'Рвота', 'Головная боль', 'Бессонница'], 
    effectiveness: 0.72 
  },
  { 
    id: '8', 
    name: 'Метоклопрамид', 
    description: 'Противорвотное средство, используемое для лечения тошноты и рвоты.', 
    dosage: 'Взрослым: 10 мг 3 раза в сутки.', 
    sideEffects: ['Сонливость', 'Беспокойство', 'Экстрапирамидные расстройства'], 
    effectiveness: 0.76 
  }
];

// Функция для получения результатов на основе симптомов
export const getResultsBySymptoms = (selectedSymptomIds: string[]): Result => {
  // Простая логика для демонстрации
  if (selectedSymptomIds.includes('4') && (selectedSymptomIds.includes('5') || selectedSymptomIds.includes('6') || selectedSymptomIds.includes('7'))) {
    // Грипп
    return {
      disease: diseases[0],
      medications: [medications[0], medications[1], medications[6]]
    };
  } else if (selectedSymptomIds.includes('1') && selectedSymptomIds.includes('2')) {
    // Мигрень
    return {
      disease: diseases[1],
      medications: [medications[2], medications[0], medications[7]]
    };
  } else if (selectedSymptomIds.includes('8') && selectedSymptomIds.includes('9')) {
    // Гастроэнтерит
    return {
      disease: diseases[2],
      medications: [medications[3], medications[7]]
    };
  } else if (selectedSymptomIds.includes('7') && (selectedSymptomIds.includes('10') || selectedSymptomIds.includes('11'))) {
    // Аллергический ринит
    return {
      disease: diseases[3],
      medications: [medications[4]]
    };
  } else if (selectedSymptomIds.includes('12') && selectedSymptomIds.includes('13')) {
    // Артрит
    return {
      disease: diseases[4],
      medications: [medications[5], medications[1]]
    };
  } else {
    // Если не удалось определить заболевание, возвращаем первое по умолчанию
    return {
      disease: diseases[0],
      medications: [medications[0], medications[1]]
    };
  }
};

// Мок-данные для аналитики
export const analyticsData: AnalyticsData = {
  symptomStats: [
    { symptomName: 'Головная боль', count: 245 },
    { symptomName: 'Тошнота', count: 180 },
    { symptomName: 'Головокружение', count: 135 },
    { symptomName: 'Повышенная температура', count: 210 },
    { symptomName: 'Боль в горле', count: 175 },
    { symptomName: 'Кашель', count: 190 },
    { symptomName: 'Насморк', count: 220 },
    { symptomName: 'Боль в животе', count: 150 },
    { symptomName: 'Диарея', count: 120 },
    { symptomName: 'Сыпь', count: 90 }
  ],
  medicationStats: [
    { medicationName: 'Парацетамол', effectiveness: 0.75, reviewCount: 320 },
    { medicationName: 'Ибупрофен', effectiveness: 0.82, reviewCount: 280 },
    { medicationName: 'Суматриптан', effectiveness: 0.88, reviewCount: 150 },
    { medicationName: 'Лоперамид', effectiveness: 0.79, reviewCount: 110 },
    { medicationName: 'Цетиризин', effectiveness: 0.85, reviewCount: 190 },
    { medicationName: 'Диклофенак', effectiveness: 0.81, reviewCount: 170 },
    { medicationName: 'Осельтамивир', effectiveness: 0.72, reviewCount: 130 },
    { medicationName: 'Метоклопрамид', effectiveness: 0.76, reviewCount: 95 }
  ],
  diseaseStats: [
    { diseaseName: 'Грипп', averageEffectiveness: 0.74 },
    { diseaseName: 'Мигрень', averageEffectiveness: 0.82 },
    { diseaseName: 'Гастроэнтерит', averageEffectiveness: 0.78 },
    { diseaseName: 'Аллергический ринит', averageEffectiveness: 0.85 },
    { diseaseName: 'Артрит', averageEffectiveness: 0.81 }
  ]
};
