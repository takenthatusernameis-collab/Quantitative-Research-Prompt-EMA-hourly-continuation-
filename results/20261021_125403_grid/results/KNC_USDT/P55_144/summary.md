# EMA Hourly Continuation — KNC/USDT P55_144

**Symbol:** KNC/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 390 |
| net_profit_factor | 0.6811 |
| net_win_rate | 0.4897 |
| gross_profit_factor | 0.9395 |
| gross_win_rate | 0.4897 |
| sharpe_ratio | -2.3245 |
| sortino_ratio | -0.6569 |
| max_drawdown | 0.5807 |
| cagr | -0.2591 |
| net_avg_win | 59.1658 |
| net_avg_loss | -83.3789 |
| avg_hold_time_bars | 15.2667 |
| exposure | 0.2706 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
