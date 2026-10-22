# EMA Hourly Continuation — SYN/USDT P89_200

**Symbol:** SYN/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 268 |
| net_profit_factor | 0.7610 |
| net_win_rate | 0.4851 |
| gross_profit_factor | 0.9315 |
| gross_win_rate | 0.4851 |
| sharpe_ratio | -1.3536 |
| sortino_ratio | -0.3163 |
| max_drawdown | 0.3294 |
| cagr | -0.1358 |
| net_avg_win | 75.1629 |
| net_avg_loss | -93.0480 |
| avg_hold_time_bars | 20.0336 |
| exposure | 0.2440 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
