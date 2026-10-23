# EMA Hourly Continuation — TAIKO/USDT P89_100

**Symbol:** TAIKO/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 469 |
| net_profit_factor | 0.2482 |
| net_win_rate | 0.3710 |
| gross_profit_factor | 0.6937 |
| gross_win_rate | 0.4350 |
| sharpe_ratio | -8.9328 |
| sortino_ratio | -2.9180 |
| max_drawdown | 0.9752 |
| cagr | -0.7863 |
| net_avg_win | 18.4930 |
| net_avg_loss | -43.9397 |
| avg_hold_time_bars | 2.2217 |
| exposure | 0.0501 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
