# EMA Hourly Continuation — ONT/USDT P8_20

**Symbol:** ONT/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1601 |
| net_profit_factor | 0.4382 |
| net_win_rate | 0.4235 |
| gross_profit_factor | 0.9766 |
| gross_win_rate | 0.4510 |
| sharpe_ratio | -12.2137 |
| sortino_ratio | -6.8891 |
| max_drawdown | 0.9999 |
| cagr | -0.9699 |
| net_avg_win | 11.5012 |
| net_avg_loss | -19.2810 |
| avg_hold_time_bars | 3.1156 |
| exposure | 0.2257 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
