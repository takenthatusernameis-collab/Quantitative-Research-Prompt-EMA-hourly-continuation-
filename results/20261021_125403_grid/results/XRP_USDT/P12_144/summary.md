# EMA Hourly Continuation — XRP/USDT P12_144

**Symbol:** XRP/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 338 |
| net_profit_factor | 0.8192 |
| net_win_rate | 0.5207 |
| gross_profit_factor | 1.0803 |
| gross_win_rate | 0.5207 |
| sharpe_ratio | -1.1024 |
| sortino_ratio | -0.2914 |
| max_drawdown | 0.3414 |
| cagr | -0.1266 |
| net_avg_win | 74.1892 |
| net_avg_loss | -98.3860 |
| avg_hold_time_bars | 42.7870 |
| exposure | 0.6574 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
