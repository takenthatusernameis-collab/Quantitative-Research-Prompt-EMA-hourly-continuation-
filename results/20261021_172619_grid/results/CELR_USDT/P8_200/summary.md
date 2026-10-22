# EMA Hourly Continuation — CELR/USDT P8_200

**Symbol:** CELR/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 290 |
| net_profit_factor | 0.7102 |
| net_win_rate | 0.4586 |
| gross_profit_factor | 0.8526 |
| gross_win_rate | 0.4586 |
| sharpe_ratio | -1.8683 |
| sortino_ratio | -0.4502 |
| max_drawdown | 0.4162 |
| cagr | -0.1879 |
| net_avg_win | 75.2746 |
| net_avg_loss | -89.7891 |
| avg_hold_time_bars | 62.7586 |
| exposure | 0.8236 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
