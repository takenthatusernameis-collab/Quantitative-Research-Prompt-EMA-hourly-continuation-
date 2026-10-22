# EMA Hourly Continuation — KAS/USDT P12_100

**Symbol:** KAS/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 745 |
| net_profit_factor | 0.5380 |
| net_win_rate | 0.4752 |
| gross_profit_factor | 0.8906 |
| gross_win_rate | 0.4846 |
| sharpe_ratio | -4.7027 |
| sortino_ratio | -1.8013 |
| max_drawdown | 0.8915 |
| cagr | -0.5830 |
| net_avg_win | 29.2366 |
| net_avg_loss | -49.2013 |
| avg_hold_time_bars | 16.4081 |
| exposure | 0.5556 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
