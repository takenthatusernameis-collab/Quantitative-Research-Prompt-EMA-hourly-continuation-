# EMA Hourly Continuation — NEO/USDT P26_50

**Symbol:** NEO/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 978 |
| net_profit_factor | 0.3201 |
| net_win_rate | 0.4029 |
| gross_profit_factor | 0.7145 |
| gross_win_rate | 0.4305 |
| sharpe_ratio | -9.9314 |
| sortino_ratio | -4.3965 |
| max_drawdown | 0.9962 |
| cagr | -0.8915 |
| net_avg_win | 11.9042 |
| net_avg_loss | -25.0898 |
| avg_hold_time_bars | 3.8374 |
| exposure | 0.1706 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
