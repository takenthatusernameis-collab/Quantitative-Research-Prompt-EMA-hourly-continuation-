# EMA Hourly Continuation — ENA/USDT P8_20

**Symbol:** ENA/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1678 |
| net_profit_factor | 0.4419 |
| net_win_rate | 0.4440 |
| gross_profit_factor | 0.7782 |
| gross_win_rate | 0.4541 |
| sharpe_ratio | -9.8995 |
| sortino_ratio | -5.7047 |
| max_drawdown | 0.9992 |
| cagr | -0.9399 |
| net_avg_win | 10.6192 |
| net_avg_loss | -19.1884 |
| avg_hold_time_bars | 2.7110 |
| exposure | 0.2068 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
