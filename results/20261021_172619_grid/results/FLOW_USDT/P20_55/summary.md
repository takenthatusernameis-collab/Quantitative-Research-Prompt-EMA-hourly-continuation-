# EMA Hourly Continuation — FLOW/USDT P20_55

**Symbol:** FLOW/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 550 |
| net_profit_factor | 0.6703 |
| net_win_rate | 0.4709 |
| gross_profit_factor | 0.9159 |
| gross_win_rate | 0.4709 |
| sharpe_ratio | -3.1198 |
| sortino_ratio | -1.0440 |
| max_drawdown | 0.7137 |
| cagr | -0.3809 |
| net_avg_win | 54.9519 |
| net_avg_loss | -72.9653 |
| avg_hold_time_bars | 8.4891 |
| exposure | 0.2122 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
