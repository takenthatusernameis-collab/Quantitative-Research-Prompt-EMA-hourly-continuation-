# EMA Hourly Continuation — ONT/USDT P8_55

**Symbol:** ONT/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 692 |
| net_profit_factor | 0.7869 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 1.0022 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -2.0360 |
| sortino_ratio | -0.7654 |
| max_drawdown | 0.6166 |
| cagr | -0.2971 |
| net_avg_win | 62.8740 |
| net_avg_loss | -79.8973 |
| avg_hold_time_bars | 13.8671 |
| exposure | 0.4342 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
