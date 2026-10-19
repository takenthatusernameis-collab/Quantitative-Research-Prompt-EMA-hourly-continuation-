# EMA Hourly Continuation — DOT/USDT P50_144

**Symbol:** DOT/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 459 |
| net_profit_factor | 0.5777 |
| net_win_rate | 0.4553 |
| gross_profit_factor | 0.9104 |
| gross_win_rate | 0.4641 |
| sharpe_ratio | -4.0310 |
| sortino_ratio | -1.2112 |
| max_drawdown | 0.7733 |
| cagr | -0.4462 |
| net_avg_win | 50.6107 |
| net_avg_loss | -73.2406 |
| avg_hold_time_bars | 12.5098 |
| exposure | 0.2610 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
