# EMA Hourly Continuation — UQC/USDT P21_144

**Symbol:** UQC/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 199 |
| net_profit_factor | 0.3661 |
| net_win_rate | 0.3065 |
| gross_profit_factor | 0.4516 |
| gross_win_rate | 0.3065 |
| sharpe_ratio | -4.3454 |
| sortino_ratio | -0.8508 |
| max_drawdown | 0.6398 |
| cagr | -0.3330 |
| net_avg_win | 60.5811 |
| net_avg_loss | -73.1438 |
| avg_hold_time_bars | 76.2111 |
| exposure | 0.6864 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
