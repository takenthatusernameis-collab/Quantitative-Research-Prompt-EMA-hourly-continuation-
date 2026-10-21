# EMA Hourly Continuation — ATOM/USDT P89_200

**Symbol:** ATOM/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 246 |
| net_profit_factor | 0.7263 |
| net_win_rate | 0.4959 |
| gross_profit_factor | 0.9616 |
| gross_win_rate | 0.4959 |
| sharpe_ratio | -1.4364 |
| sortino_ratio | -0.3229 |
| max_drawdown | 0.3104 |
| cagr | -0.1375 |
| net_avg_win | 67.5022 |
| net_avg_loss | -91.4437 |
| avg_hold_time_bars | 15.9350 |
| exposure | 0.1782 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
