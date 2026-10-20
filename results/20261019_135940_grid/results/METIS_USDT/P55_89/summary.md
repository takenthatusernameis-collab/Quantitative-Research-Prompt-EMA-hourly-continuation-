# EMA Hourly Continuation — METIS/USDT P55_89

**Symbol:** METIS/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 695 |
| net_profit_factor | 0.3960 |
| net_win_rate | 0.4086 |
| gross_profit_factor | 0.7485 |
| gross_win_rate | 0.4230 |
| sharpe_ratio | -7.5220 |
| sortino_ratio | -2.8114 |
| max_drawdown | 0.9696 |
| cagr | -0.7496 |
| net_avg_win | 22.3720 |
| net_avg_loss | -39.0383 |
| avg_hold_time_bars | 4.0086 |
| exposure | 0.1266 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
