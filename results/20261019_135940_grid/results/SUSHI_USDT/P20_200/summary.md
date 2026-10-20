# EMA Hourly Continuation — SUSHI/USDT P20_200

**Symbol:** SUSHI/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 440 |
| net_profit_factor | 0.6242 |
| net_win_rate | 0.4750 |
| gross_profit_factor | 0.9029 |
| gross_win_rate | 0.4795 |
| sharpe_ratio | -2.8961 |
| sortino_ratio | -0.8491 |
| max_drawdown | 0.6514 |
| cagr | -0.3355 |
| net_avg_win | 51.1406 |
| net_avg_loss | -74.1222 |
| avg_hold_time_bars | 29.7250 |
| exposure | 0.5918 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
