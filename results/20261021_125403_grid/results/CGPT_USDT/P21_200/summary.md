# EMA Hourly Continuation — CGPT/USDT P21_200

**Symbol:** CGPT/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 285 |
| net_profit_factor | 0.7703 |
| net_win_rate | 0.4737 |
| gross_profit_factor | 0.8924 |
| gross_win_rate | 0.4737 |
| sharpe_ratio | -1.3341 |
| sortino_ratio | -0.3202 |
| max_drawdown | 0.3176 |
| cagr | -0.1380 |
| net_avg_win | 77.3413 |
| net_avg_loss | -90.3596 |
| avg_hold_time_bars | 46.4877 |
| exposure | 0.6022 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
