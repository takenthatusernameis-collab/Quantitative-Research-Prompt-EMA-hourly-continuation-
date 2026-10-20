# EMA Hourly Continuation — DEEP/USDT P12_21

**Symbol:** DEEP/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1109 |
| net_profit_factor | 0.5701 |
| net_win_rate | 0.4400 |
| gross_profit_factor | 0.9624 |
| gross_win_rate | 0.4599 |
| sharpe_ratio | -9.7267 |
| sortino_ratio | -5.0783 |
| max_drawdown | 0.9946 |
| cagr | -0.9231 |
| net_avg_win | 27.0221 |
| net_avg_loss | -37.2465 |
| avg_hold_time_bars | 2.3237 |
| exposure | 0.1459 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
