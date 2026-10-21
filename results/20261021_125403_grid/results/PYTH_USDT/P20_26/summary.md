# EMA Hourly Continuation — PYTH/USDT P20_26

**Symbol:** PYTH/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 180 |
| net_profit_factor | 0.7174 |
| net_win_rate | 0.4833 |
| gross_profit_factor | 0.9572 |
| gross_win_rate | 0.4833 |
| sharpe_ratio | -1.4952 |
| sortino_ratio | -0.2870 |
| max_drawdown | 0.3442 |
| cagr | -0.1234 |
| net_avg_win | 82.1917 |
| net_avg_loss | -107.1723 |
| avg_hold_time_bars | 4.0000 |
| exposure | 0.0327 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
