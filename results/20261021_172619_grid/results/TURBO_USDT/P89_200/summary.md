# EMA Hourly Continuation — TURBO/USDT P89_200

**Symbol:** TURBO/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 246 |
| net_profit_factor | 0.8979 |
| net_win_rate | 0.5285 |
| gross_profit_factor | 1.1022 |
| gross_win_rate | 0.5285 |
| sharpe_ratio | -0.5054 |
| sortino_ratio | -0.1253 |
| max_drawdown | 0.2028 |
| cagr | -0.0588 |
| net_avg_win | 80.5365 |
| net_avg_loss | -100.5210 |
| avg_hold_time_bars | 14.1748 |
| exposure | 0.1902 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
