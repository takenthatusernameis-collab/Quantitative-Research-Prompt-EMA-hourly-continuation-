# EMA Hourly Continuation — TNSR/USDT P21_89

**Symbol:** TNSR/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 714 |
| net_profit_factor | 0.7224 |
| net_win_rate | 0.4916 |
| gross_profit_factor | 1.0243 |
| gross_win_rate | 0.5014 |
| sharpe_ratio | -3.1864 |
| sortino_ratio | -1.1998 |
| max_drawdown | 0.7833 |
| cagr | -0.4334 |
| net_avg_win | 56.4635 |
| net_avg_loss | -75.5735 |
| avg_hold_time_bars | 11.5882 |
| exposure | 0.3744 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
