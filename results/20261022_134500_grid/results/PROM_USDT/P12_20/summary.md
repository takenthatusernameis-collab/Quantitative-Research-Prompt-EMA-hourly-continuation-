# EMA Hourly Continuation — PROM/USDT P12_20

**Symbol:** PROM/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1432 |
| net_profit_factor | 0.3687 |
| net_win_rate | 0.3652 |
| gross_profit_factor | 0.9108 |
| gross_win_rate | 0.4190 |
| sharpe_ratio | -14.4062 |
| sortino_ratio | -7.7874 |
| max_drawdown | 1.0000 |
| cagr | -0.9827 |
| net_avg_win | 11.1652 |
| net_avg_loss | -17.4247 |
| avg_hold_time_bars | 3.0189 |
| exposure | 0.1965 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
