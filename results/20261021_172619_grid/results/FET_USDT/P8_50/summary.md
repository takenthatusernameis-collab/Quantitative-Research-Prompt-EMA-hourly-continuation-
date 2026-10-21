# EMA Hourly Continuation — FET/USDT P8_50

**Symbol:** FET/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 690 |
| net_profit_factor | 0.8733 |
| net_win_rate | 0.5101 |
| gross_profit_factor | 1.0535 |
| gross_win_rate | 0.5101 |
| sharpe_ratio | -1.2410 |
| sortino_ratio | -0.4681 |
| max_drawdown | 0.5185 |
| cagr | -0.1975 |
| net_avg_win | 83.1607 |
| net_avg_loss | -99.1651 |
| avg_hold_time_bars | 12.7101 |
| exposure | 0.3986 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
