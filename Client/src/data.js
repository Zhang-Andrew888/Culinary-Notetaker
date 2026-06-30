// Sample data. Field names mirror the documented MiseNote API
// (dish_name, cuisine_area, steps[], ingredients[{name, amount}],
// book_name, recipe_ids[]) so wiring a real backend later is a swap, not a
// rewrite. `author` / `link` are the optional fields added on the Create form.

export const recipes = [
  {
    id: 1,
    dish_name: 'Pasta Carbonara',
    cuisine_area: 'Italian',
    description: 'Silky egg, pecorino, and crisp guanciale — no cream, ever.',
    author: 'Andrew Chen',
    link: '',
    ingredients: [
      { name: 'Spaghetti', amount: '400 g' },
      { name: 'Eggs', amount: '4' },
      { name: 'Pecorino Romano', amount: '100 g' },
      { name: 'Guanciale', amount: '150 g' },
    ],
    steps: [
      'Boil the spaghetti in well-salted water until al dente. Reserve a mug of pasta water before draining.',
      'Whisk the eggs with grated pecorino and a heavy crack of black pepper.',
      'Crisp the guanciale, kill the heat, toss in the pasta, then fold through the egg mixture — loosen with pasta water until glossy.',
    ],
  },
  {
    id: 2,
    dish_name: 'Miso-Glazed Salmon',
    cuisine_area: 'Japanese',
    description: 'Sweet-savory miso glaze, broiled until caramelized.',
    author: '',
    link: '',
    ingredients: [
      { name: 'Salmon fillets', amount: '4' },
      { name: 'White miso', amount: '3 tbsp' },
      { name: 'Mirin', amount: '2 tbsp' },
      { name: 'Sake', amount: '2 tbsp' },
    ],
    steps: [
      'Whisk miso, mirin, and sake into a smooth glaze.',
      'Marinate the salmon for 30 minutes.',
      'Broil until caramelized and just cooked through.',
    ],
  },
  {
    id: 3,
    dish_name: 'Shakshuka',
    cuisine_area: 'Levantine',
    description: 'Eggs poached in a spiced tomato and pepper stew.',
    author: '',
    link: '',
    ingredients: [
      { name: 'Eggs', amount: '6' },
      { name: 'Crushed tomatoes', amount: '800 g' },
      { name: 'Red pepper', amount: '1' },
      { name: 'Cumin', amount: '1 tsp' },
    ],
    steps: [
      'Soften onion and pepper, then bloom the spices.',
      'Simmer the tomatoes until jammy.',
      'Make wells, crack in the eggs, cover, and poach.',
    ],
  },
  {
    id: 4,
    dish_name: 'Tacos al Pastor',
    cuisine_area: 'Mexican',
    description: 'Achiote-marinated pork with charred pineapple.',
    author: '',
    link: '',
    ingredients: [
      { name: 'Pork shoulder', amount: '1 kg' },
      { name: 'Achiote paste', amount: '3 tbsp' },
      { name: 'Pineapple', amount: '1/2' },
      { name: 'Corn tortillas', amount: '12' },
    ],
    steps: [
      'Marinate the pork in achiote overnight.',
      'Sear and roast until tender, then chop.',
      'Char the pineapple and build the tacos.',
    ],
  },
  {
    id: 5,
    dish_name: 'Green Curry',
    cuisine_area: 'Thai',
    description: 'Fragrant coconut curry finished with Thai basil.',
    author: '',
    link: '',
    ingredients: [
      { name: 'Green curry paste', amount: '3 tbsp' },
      { name: 'Coconut milk', amount: '400 ml' },
      { name: 'Chicken thigh', amount: '500 g' },
    ],
    steps: [
      'Fry the curry paste until fragrant.',
      'Add coconut milk and bring to a gentle simmer.',
      'Add chicken and vegetables; finish with basil.',
    ],
  },
  {
    id: 6,
    dish_name: 'Ramen',
    cuisine_area: 'Japanese',
    description: 'Slow-simmered broth with springy noodles.',
    author: '',
    link: '',
    ingredients: [
      { name: 'Ramen noodles', amount: '4 portions' },
      { name: 'Stock', amount: '2 L' },
      { name: 'Soft eggs', amount: '4' },
    ],
    steps: [
      'Simmer the broth low and slow.',
      'Cook the noodles to the bite.',
      'Assemble with toppings and a soft egg.',
    ],
  },
];

export const logsByRecipe = {
  1: [
    { date: '2026-06-18', notes: 'Reduced guanciale to 120 g — less greasy, better balance.' },
    { date: '2026-05-30', notes: 'Added more salt to the pasta water. Tasted right.' },
    { date: '2026-05-12', notes: 'First attempt. Eggs scrambled slightly — lower the heat next time.' },
  ],
};

export const cookbooks = [
  {
    id: 1,
    book_name: 'Weeknight Dinners',
    description: 'Quick meals under 30 minutes.',
    recipe_count: 5,
    recipe_ids: [1, 3, 4],
  },
  {
    id: 2,
    book_name: 'Sunday Baking',
    description: 'Slow mornings, warm ovens, too much butter.',
    recipe_count: 8,
    recipe_ids: [2, 5],
  },
  {
    id: 3,
    book_name: 'Date Night',
    description: 'Dishes worth lingering over.',
    recipe_count: 3,
    recipe_ids: [1, 6],
  },
];
