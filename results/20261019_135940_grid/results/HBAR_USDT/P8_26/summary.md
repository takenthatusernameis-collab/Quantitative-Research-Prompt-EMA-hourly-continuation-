# EMA Hourly Continuation — HBAR/USDT P8_26

**Symbol:** HBAR/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1655 |
| net_profit_factor | 0.4384 |
| net_win_rate | 0.4683 |
| gross_profit_factor | 0.9218 |
| gross_win_rate | 0.4852 |
| sharpe_ratio | -10.1675 |
| sortino_ratio | -5.8140 |
| max_drawdown | 0.9994 |
| cagr | -0.9465 |
| net_avg_win | 10.0658 |
| net_avg_loss | -20.2211 |
| avg_hold_time_bars | 3.4683 |
| exposure | 0.2609 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
