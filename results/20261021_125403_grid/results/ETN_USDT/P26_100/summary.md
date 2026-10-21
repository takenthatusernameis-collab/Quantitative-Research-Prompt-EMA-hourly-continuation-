# EMA Hourly Continuation — ETN/USDT P26_100

**Symbol:** ETN/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 372 |
| net_profit_factor | 0.5977 |
| net_win_rate | 0.4247 |
| gross_profit_factor | 0.7449 |
| gross_win_rate | 0.4247 |
| sharpe_ratio | -3.4939 |
| sortino_ratio | -1.0407 |
| max_drawdown | 0.6415 |
| cagr | -0.3820 |
| net_avg_win | 59.8185 |
| net_avg_loss | -73.8972 |
| avg_hold_time_bars | 15.1747 |
| exposure | 0.3066 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
