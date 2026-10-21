# EMA Hourly Continuation — SHIB/USDT P8_26

**Symbol:** SHIB/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 580 |
| net_profit_factor | 0.7662 |
| net_win_rate | 0.5155 |
| gross_profit_factor | 1.0769 |
| gross_win_rate | 0.5155 |
| sharpe_ratio | -2.1703 |
| sortino_ratio | -0.7532 |
| max_drawdown | 0.5986 |
| cagr | -0.2913 |
| net_avg_win | 63.4304 |
| net_avg_loss | -88.0906 |
| avg_hold_time_bars | 6.7724 |
| exposure | 0.1785 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
