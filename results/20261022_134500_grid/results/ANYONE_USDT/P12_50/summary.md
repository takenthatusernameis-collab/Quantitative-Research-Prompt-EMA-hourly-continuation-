# EMA Hourly Continuation — ANYONE/USDT P12_50

**Symbol:** ANYONE/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 923 |
| net_profit_factor | 0.5947 |
| net_win_rate | 0.4410 |
| gross_profit_factor | 0.8051 |
| gross_win_rate | 0.4431 |
| sharpe_ratio | -5.4042 |
| sortino_ratio | -2.4335 |
| max_drawdown | 0.9271 |
| cagr | -0.6839 |
| net_avg_win | 33.3797 |
| net_avg_loss | -44.2714 |
| avg_hold_time_bars | 7.5980 |
| exposure | 0.3544 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
