# EMA Hourly Continuation — THETA/USDT P100_200

**Symbol:** THETA/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 389 |
| net_profit_factor | 0.6119 |
| net_win_rate | 0.4859 |
| gross_profit_factor | 0.9721 |
| gross_win_rate | 0.4987 |
| sharpe_ratio | -2.8010 |
| sortino_ratio | -0.7834 |
| max_drawdown | 0.6147 |
| cagr | -0.3081 |
| net_avg_win | 50.3436 |
| net_avg_loss | -77.7482 |
| avg_hold_time_bars | 8.6864 |
| exposure | 0.1536 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
