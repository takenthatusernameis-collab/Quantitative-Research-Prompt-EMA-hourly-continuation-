# EMA Hourly Continuation — HNT/USDT P55_89

**Symbol:** HNT/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 756 |
| net_profit_factor | 0.4493 |
| net_win_rate | 0.4365 |
| gross_profit_factor | 0.7759 |
| gross_win_rate | 0.4511 |
| sharpe_ratio | -6.3923 |
| sortino_ratio | -2.4928 |
| max_drawdown | 0.9536 |
| cagr | -0.6970 |
| net_avg_win | 23.4895 |
| net_avg_loss | -40.5003 |
| avg_hold_time_bars | 4.3294 |
| exposure | 0.1488 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
