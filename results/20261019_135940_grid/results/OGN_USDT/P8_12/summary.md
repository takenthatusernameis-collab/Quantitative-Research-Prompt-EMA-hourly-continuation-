# EMA Hourly Continuation — OGN/USDT P8_12

**Symbol:** OGN/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1703 |
| net_profit_factor | 0.2330 |
| net_win_rate | 0.3846 |
| gross_profit_factor | 0.8552 |
| gross_win_rate | 0.4551 |
| sharpe_ratio | -15.9945 |
| sortino_ratio | -9.4716 |
| max_drawdown | 1.0000 |
| cagr | -0.9934 |
| net_avg_win | 4.6376 |
| net_avg_loss | -12.4405 |
| avg_hold_time_bars | 2.1897 |
| exposure | 0.1687 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
