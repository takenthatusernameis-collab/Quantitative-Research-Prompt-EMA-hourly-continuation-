# EMA Hourly Continuation — XYO/USDT P12_26

**Symbol:** XYO/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 533 |
| net_profit_factor | 0.6262 |
| net_win_rate | 0.4747 |
| gross_profit_factor | 0.9444 |
| gross_win_rate | 0.4747 |
| sharpe_ratio | -3.8009 |
| sortino_ratio | -1.2548 |
| max_drawdown | 0.7757 |
| cagr | -0.4389 |
| net_avg_win | 50.8004 |
| net_avg_loss | -73.3016 |
| avg_hold_time_bars | 6.1351 |
| exposure | 0.1480 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
