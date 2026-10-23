# EMA Hourly Continuation — API3/USDT P8_100

**Symbol:** API3/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 720 |
| net_profit_factor | 0.6228 |
| net_win_rate | 0.4625 |
| gross_profit_factor | 0.9215 |
| gross_win_rate | 0.4764 |
| sharpe_ratio | -4.1857 |
| sortino_ratio | -1.5722 |
| max_drawdown | 0.8576 |
| cagr | -0.5293 |
| net_avg_win | 42.1165 |
| net_avg_loss | -58.1845 |
| avg_hold_time_bars | 19.9986 |
| exposure | 0.6545 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
