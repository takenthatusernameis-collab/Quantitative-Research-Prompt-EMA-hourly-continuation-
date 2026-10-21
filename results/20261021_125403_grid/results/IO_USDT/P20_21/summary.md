# EMA Hourly Continuation — IO/USDT P20_21

**Symbol:** IO/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 107 |
| net_profit_factor | 0.7639 |
| net_win_rate | 0.4953 |
| gross_profit_factor | 0.9755 |
| gross_win_rate | 0.4953 |
| sharpe_ratio | -0.8847 |
| sortino_ratio | -0.1353 |
| max_drawdown | 0.1684 |
| cagr | -0.0603 |
| net_avg_win | 83.3383 |
| net_avg_loss | -107.0734 |
| avg_hold_time_bars | 4.6449 |
| exposure | 0.0241 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
