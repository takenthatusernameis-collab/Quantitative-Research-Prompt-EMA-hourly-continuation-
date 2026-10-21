# EMA Hourly Continuation — AXS/USDT P50_89

**Symbol:** AXS/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 331 |
| net_profit_factor | 0.8019 |
| net_win_rate | 0.5287 |
| gross_profit_factor | 1.1156 |
| gross_win_rate | 0.5287 |
| sharpe_ratio | -1.2373 |
| sortino_ratio | -0.3242 |
| max_drawdown | 0.4176 |
| cagr | -0.1390 |
| net_avg_win | 72.7312 |
| net_avg_loss | -101.7412 |
| avg_hold_time_bars | 7.6737 |
| exposure | 0.1149 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
