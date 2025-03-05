<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Stock Portfolio Tracker</title>
    <style>
        body { font-family: Arial, sans-serif; text-align: center; }
        table { width: 80%; margin: 20px auto; border-collapse: collapse; }
        th, td { border: 1px solid black; padding: 10px; }
    </style>
</head>
<body>
    <h2>Stock Portfolio Tracker</h2>
    <input type="text" id="stockSymbol" placeholder="Enter stock symbol">
    <button onclick="addStock()">Add Stock</button>
    <table>
        <thead>
            <tr>
                <th>Stock</th>
                <th>Price</th>
                <th>Change</th>
                <th>Actions</th>
            </tr>
        </thead>
        <tbody id="portfolio"></tbody>
    </table>

    <script>
        async function fetchStockData(symbol) {
            // Placeholder for fetching real stock data
            return { symbol: symbol.toUpperCase(), price: (Math.random() * 1000).toFixed(2), change: (Math.random() * 10 - 5).toFixed(2) };
        }

        async function addStock() {
            const symbol = document.getElementById('stockSymbol').value;
            if (!symbol) return;

            const stockData = await fetchStockData(symbol);
            const row = document.createElement('tr');
            row.innerHTML = `<td>${stockData.symbol}</td>
                             <td>$${stockData.price}</td>
                             <td>${stockData.change}%</td>
                             <td><button onclick="removeStock(this)">Remove</button></td>`;
            document.getElementById('portfolio').appendChild(row);
            document.getElementById('stockSymbol').value = '';
        }

        function removeStock(button) {
            button.parentElement.parentElement.remove();
        }
    </script>
</body>
</html>
