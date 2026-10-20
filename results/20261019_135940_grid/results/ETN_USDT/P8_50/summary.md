# EMA Hourly Continuation — ETN/USDT P8_50

**Symbol:** ETN/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1064 |
| net_profit_factor | 0.3926 |
| net_win_rate | 0.3665 |
| gross_profit_factor | 0.5711 |
| gross_win_rate | 0.3731 |
| sharpe_ratio | -11.1043 |
| sortino_ratio | -5.5352 |
| max_drawdown | 0.9972 |
| cagr | -0.9377 |
| net_avg_win | 16.5279 |
| net_avg_loss | -24.3570 |
| avg_hold_time_bars | 7.4596 |
| exposure | 0.4311 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
