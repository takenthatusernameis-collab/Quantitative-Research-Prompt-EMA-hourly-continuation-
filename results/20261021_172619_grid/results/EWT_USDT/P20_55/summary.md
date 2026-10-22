# EMA Hourly Continuation — EWT/USDT P20_55

**Symbol:** EWT/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 451 |
| net_profit_factor | 0.6969 |
| net_win_rate | 0.4767 |
| gross_profit_factor | 0.9034 |
| gross_win_rate | 0.4767 |
| sharpe_ratio | -2.3855 |
| sortino_ratio | -0.7226 |
| max_drawdown | 0.5697 |
| cagr | -0.2826 |
| net_avg_win | 60.4963 |
| net_avg_loss | -79.0851 |
| avg_hold_time_bars | 9.1973 |
| exposure | 0.1885 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
