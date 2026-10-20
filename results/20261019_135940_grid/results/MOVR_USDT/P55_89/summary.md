# EMA Hourly Continuation — MOVR/USDT P55_89

**Symbol:** MOVR/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 702 |
| net_profit_factor | 0.3973 |
| net_win_rate | 0.4245 |
| gross_profit_factor | 0.7364 |
| gross_win_rate | 0.4330 |
| sharpe_ratio | -6.9101 |
| sortino_ratio | -2.5956 |
| max_drawdown | 0.9591 |
| cagr | -0.7162 |
| net_avg_win | 21.1878 |
| net_avg_loss | -39.3339 |
| avg_hold_time_bars | 4.1595 |
| exposure | 0.1327 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
