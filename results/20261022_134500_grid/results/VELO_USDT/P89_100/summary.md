# EMA Hourly Continuation — VELO/USDT P89_100

**Symbol:** VELO/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 609 |
| net_profit_factor | 0.3165 |
| net_win_rate | 0.3941 |
| gross_profit_factor | 0.6236 |
| gross_win_rate | 0.4236 |
| sharpe_ratio | -8.3186 |
| sortino_ratio | -2.9397 |
| max_drawdown | 0.9779 |
| cagr | -0.7795 |
| net_avg_win | 18.8626 |
| net_avg_loss | -38.7601 |
| avg_hold_time_bars | 2.3612 |
| exposure | 0.0654 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
