# EMA Hourly Continuation — AAVE/USDT P34_100

**Symbol:** AAVE/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 371 |
| net_profit_factor | 0.8523 |
| net_win_rate | 0.5148 |
| gross_profit_factor | 1.0697 |
| gross_win_rate | 0.5148 |
| sharpe_ratio | -1.0322 |
| sortino_ratio | -0.2859 |
| max_drawdown | 0.3845 |
| cagr | -0.1247 |
| net_avg_win | 85.8857 |
| net_avg_loss | -106.9282 |
| avg_hold_time_bars | 15.1968 |
| exposure | 0.2563 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
