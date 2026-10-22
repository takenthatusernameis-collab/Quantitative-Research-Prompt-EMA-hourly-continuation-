# EMA Hourly Continuation — API3/USDT P26_55

**Symbol:** API3/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 455 |
| net_profit_factor | 0.7343 |
| net_win_rate | 0.4989 |
| gross_profit_factor | 0.9919 |
| gross_win_rate | 0.4989 |
| sharpe_ratio | -2.1461 |
| sortino_ratio | -0.6560 |
| max_drawdown | 0.5418 |
| cagr | -0.2602 |
| net_avg_win | 64.6228 |
| net_avg_loss | -87.6257 |
| avg_hold_time_bars | 7.6857 |
| exposure | 0.1590 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
