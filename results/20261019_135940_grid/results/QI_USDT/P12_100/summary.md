# EMA Hourly Continuation — QI/USDT P12_100

**Symbol:** QI/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 580 |
| net_profit_factor | 0.6744 |
| net_win_rate | 0.4810 |
| gross_profit_factor | 0.9805 |
| gross_win_rate | 0.4897 |
| sharpe_ratio | -3.2185 |
| sortino_ratio | -1.0873 |
| max_drawdown | 0.7530 |
| cagr | -0.4048 |
| net_avg_win | 54.1752 |
| net_avg_loss | -74.4649 |
| avg_hold_time_bars | 21.8207 |
| exposure | 0.5727 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
