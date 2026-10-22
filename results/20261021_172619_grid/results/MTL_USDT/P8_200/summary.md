# EMA Hourly Continuation — MTL/USDT P8_200

**Symbol:** MTL/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 214 |
| net_profit_factor | 1.0831 |
| net_win_rate | 0.5654 |
| gross_profit_factor | 1.2933 |
| gross_win_rate | 0.5654 |
| sharpe_ratio | 0.4117 |
| sortino_ratio | 0.0877 |
| max_drawdown | 0.0900 |
| cagr | 0.0341 |
| net_avg_win | 95.2287 |
| net_avg_loss | -114.3959 |
| avg_hold_time_bars | 87.7991 |
| exposure | 0.8503 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
