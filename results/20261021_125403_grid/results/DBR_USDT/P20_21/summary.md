# EMA Hourly Continuation — DBR/USDT P20_21

**Symbol:** DBR/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 185 |
| net_profit_factor | 0.5917 |
| net_win_rate | 0.5081 |
| gross_profit_factor | 1.1261 |
| gross_win_rate | 0.5297 |
| sharpe_ratio | -2.3495 |
| sortino_ratio | -0.5155 |
| max_drawdown | 0.4143 |
| cagr | -0.2092 |
| net_avg_win | 57.9390 |
| net_avg_loss | -101.1427 |
| avg_hold_time_bars | 6.9135 |
| exposure | 0.0727 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
