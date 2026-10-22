# EMA Hourly Continuation — MEW/USDT P26_55

**Symbol:** MEW/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 470 |
| net_profit_factor | 0.6825 |
| net_win_rate | 0.4766 |
| gross_profit_factor | 0.8956 |
| gross_win_rate | 0.4766 |
| sharpe_ratio | -2.5755 |
| sortino_ratio | -0.7970 |
| max_drawdown | 0.6047 |
| cagr | -0.3063 |
| net_avg_win | 57.6738 |
| net_avg_loss | -76.9432 |
| avg_hold_time_bars | 6.0809 |
| exposure | 0.1299 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
