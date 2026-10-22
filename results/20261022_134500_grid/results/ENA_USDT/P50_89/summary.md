# EMA Hourly Continuation — ENA/USDT P50_89

**Symbol:** ENA/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 609 |
| net_profit_factor | 0.5933 |
| net_win_rate | 0.4614 |
| gross_profit_factor | 0.8949 |
| gross_win_rate | 0.4663 |
| sharpe_ratio | -4.4076 |
| sortino_ratio | -1.5226 |
| max_drawdown | 0.8503 |
| cagr | -0.5217 |
| net_avg_win | 43.7769 |
| net_avg_loss | -63.2085 |
| avg_hold_time_bars | 4.7898 |
| exposure | 0.1326 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
