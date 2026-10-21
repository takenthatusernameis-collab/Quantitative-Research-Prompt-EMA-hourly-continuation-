# EMA Hourly Continuation — IOTA/USDT P26_100

**Symbol:** IOTA/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 467 |
| net_profit_factor | 0.6849 |
| net_win_rate | 0.4582 |
| gross_profit_factor | 0.8684 |
| gross_win_rate | 0.4582 |
| sharpe_ratio | -2.7606 |
| sortino_ratio | -0.8481 |
| max_drawdown | 0.6606 |
| cagr | -0.3228 |
| net_avg_win | 63.3911 |
| net_avg_loss | -78.2915 |
| avg_hold_time_bars | 15.9208 |
| exposure | 0.3380 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
