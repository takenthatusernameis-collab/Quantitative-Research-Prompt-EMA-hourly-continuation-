# EMA Hourly Continuation — JASMY/USDT P8_12

**Symbol:** JASMY/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1830 |
| net_profit_factor | 0.1499 |
| net_win_rate | 0.3628 |
| gross_profit_factor | 0.3996 |
| gross_win_rate | 0.4011 |
| sharpe_ratio | -17.9767 |
| sortino_ratio | -11.0791 |
| max_drawdown | 1.0000 |
| cagr | -0.9975 |
| net_avg_win | 2.6551 |
| net_avg_loss | -10.0883 |
| avg_hold_time_bars | 1.6995 |
| exposure | 0.1414 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
