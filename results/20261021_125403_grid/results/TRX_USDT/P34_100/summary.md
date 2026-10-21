# EMA Hourly Continuation — TRX/USDT P34_100

**Symbol:** TRX/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 360 |
| net_profit_factor | 0.4469 |
| net_win_rate | 0.4583 |
| gross_profit_factor | 0.9236 |
| gross_win_rate | 0.4722 |
| sharpe_ratio | -4.9620 |
| sortino_ratio | -1.3684 |
| max_drawdown | 0.7983 |
| cagr | -0.4714 |
| net_avg_win | 39.1003 |
| net_avg_loss | -74.0253 |
| avg_hold_time_bars | 13.8528 |
| exposure | 0.2267 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
