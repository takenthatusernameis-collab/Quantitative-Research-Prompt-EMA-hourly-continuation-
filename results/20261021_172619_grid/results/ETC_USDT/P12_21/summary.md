# EMA Hourly Continuation — ETC/USDT P12_21

**Symbol:** ETC/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 327 |
| net_profit_factor | 0.6200 |
| net_win_rate | 0.5107 |
| gross_profit_factor | 1.0213 |
| gross_win_rate | 0.5107 |
| sharpe_ratio | -2.5346 |
| sortino_ratio | -0.6617 |
| max_drawdown | 0.5403 |
| cagr | -0.2599 |
| net_avg_win | 51.8082 |
| net_avg_loss | -87.2210 |
| avg_hold_time_bars | 4.5535 |
| exposure | 0.0677 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
