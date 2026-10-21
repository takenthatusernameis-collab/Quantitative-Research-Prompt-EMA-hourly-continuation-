# EMA Hourly Continuation — KAS/USDT P21_34

**Symbol:** KAS/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 240 |
| net_profit_factor | 0.9245 |
| net_win_rate | 0.5667 |
| gross_profit_factor | 1.2960 |
| gross_win_rate | 0.5667 |
| sharpe_ratio | -0.3451 |
| sortino_ratio | -0.0780 |
| max_drawdown | 0.2168 |
| cagr | -0.0376 |
| net_avg_win | 82.5968 |
| net_avg_loss | -116.8296 |
| avg_hold_time_bars | 5.1542 |
| exposure | 0.0562 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
