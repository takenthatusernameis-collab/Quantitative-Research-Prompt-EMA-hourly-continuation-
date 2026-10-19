# EMA Hourly Continuation — POL/USDT P50_55

**Symbol:** POL/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 904 |
| net_profit_factor | 0.1031 |
| net_win_rate | 0.3031 |
| gross_profit_factor | 0.3728 |
| gross_win_rate | 0.3573 |
| sharpe_ratio | -14.9287 |
| sortino_ratio | -6.7706 |
| max_drawdown | 0.9999 |
| cagr | -0.9760 |
| net_avg_win | 4.1933 |
| net_avg_loss | -17.6954 |
| avg_hold_time_bars | 1.9867 |
| exposure | 0.0816 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
