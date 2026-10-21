# EMA Hourly Continuation — SWFTC/USDT P21_26

**Symbol:** SWFTC/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 164 |
| net_profit_factor | 0.6304 |
| net_win_rate | 0.4634 |
| gross_profit_factor | 0.8761 |
| gross_win_rate | 0.4634 |
| sharpe_ratio | -1.8954 |
| sortino_ratio | -0.3466 |
| max_drawdown | 0.3534 |
| cagr | -0.1477 |
| net_avg_win | 74.1774 |
| net_avg_loss | -101.6230 |
| avg_hold_time_bars | 5.5427 |
| exposure | 0.0413 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
