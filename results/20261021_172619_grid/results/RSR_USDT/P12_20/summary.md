# EMA Hourly Continuation — RSR/USDT P12_20

**Symbol:** RSR/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 279 |
| net_profit_factor | 0.7854 |
| net_win_rate | 0.5125 |
| gross_profit_factor | 1.0409 |
| gross_win_rate | 0.5125 |
| sharpe_ratio | -1.2254 |
| sortino_ratio | -0.2945 |
| max_drawdown | 0.3482 |
| cagr | -0.1267 |
| net_avg_win | 73.8225 |
| net_avg_loss | -98.8258 |
| avg_hold_time_bars | 5.3978 |
| exposure | 0.0685 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
