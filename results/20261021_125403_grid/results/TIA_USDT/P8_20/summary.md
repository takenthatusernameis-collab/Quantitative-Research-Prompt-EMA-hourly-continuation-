# EMA Hourly Continuation — TIA/USDT P8_20

**Symbol:** TIA/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 489 |
| net_profit_factor | 0.7789 |
| net_win_rate | 0.5031 |
| gross_profit_factor | 1.0073 |
| gross_win_rate | 0.5031 |
| sharpe_ratio | -1.7384 |
| sortino_ratio | -0.5517 |
| max_drawdown | 0.5080 |
| cagr | -0.2247 |
| net_avg_win | 67.6349 |
| net_avg_loss | -87.9053 |
| avg_hold_time_bars | 5.1656 |
| exposure | 0.1148 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
