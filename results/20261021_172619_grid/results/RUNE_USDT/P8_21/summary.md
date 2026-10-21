# EMA Hourly Continuation — RUNE/USDT P8_21

**Symbol:** RUNE/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 524 |
| net_profit_factor | 0.6957 |
| net_win_rate | 0.4885 |
| gross_profit_factor | 0.9820 |
| gross_win_rate | 0.4885 |
| sharpe_ratio | -2.9300 |
| sortino_ratio | -0.9614 |
| max_drawdown | 0.6827 |
| cagr | -0.3565 |
| net_avg_win | 59.7946 |
| net_avg_loss | -82.0957 |
| avg_hold_time_bars | 5.4466 |
| exposure | 0.1297 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
