# EMA Hourly Continuation — DCR/USDT P8_200

**Symbol:** DCR/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 437 |
| net_profit_factor | 0.7885 |
| net_win_rate | 0.4989 |
| gross_profit_factor | 0.9749 |
| gross_win_rate | 0.4989 |
| sharpe_ratio | -1.4264 |
| sortino_ratio | -0.4248 |
| max_drawdown | 0.4434 |
| cagr | -0.1789 |
| net_avg_win | 67.0126 |
| net_avg_loss | -84.5979 |
| avg_hold_time_bars | 37.0092 |
| exposure | 0.7318 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
