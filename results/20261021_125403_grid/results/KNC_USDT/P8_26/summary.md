# EMA Hourly Continuation — KNC/USDT P8_26

**Symbol:** KNC/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 848 |
| net_profit_factor | 0.6308 |
| net_win_rate | 0.4741 |
| gross_profit_factor | 0.9584 |
| gross_win_rate | 0.4764 |
| sharpe_ratio | -4.8744 |
| sortino_ratio | -2.0319 |
| max_drawdown | 0.9098 |
| cagr | -0.6068 |
| net_avg_win | 38.4178 |
| net_avg_loss | -54.8977 |
| avg_hold_time_bars | 7.1486 |
| exposure | 0.2755 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
