# EMA Hourly Continuation — EUL/USDT P12_100

**Symbol:** EUL/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 696 |
| net_profit_factor | 0.5380 |
| net_win_rate | 0.4555 |
| gross_profit_factor | 0.7630 |
| gross_win_rate | 0.4598 |
| sharpe_ratio | -4.2459 |
| sortino_ratio | -1.5663 |
| max_drawdown | 0.8528 |
| cagr | -0.5306 |
| net_avg_win | 31.2407 |
| net_avg_loss | -48.5661 |
| avg_hold_time_bars | 16.9856 |
| exposure | 0.5374 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
