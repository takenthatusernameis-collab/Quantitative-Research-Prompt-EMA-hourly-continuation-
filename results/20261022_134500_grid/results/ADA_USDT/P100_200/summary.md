# EMA Hourly Continuation — ADA/USDT P100_200

**Symbol:** ADA/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 376 |
| net_profit_factor | 0.5899 |
| net_win_rate | 0.4867 |
| gross_profit_factor | 1.0380 |
| gross_win_rate | 0.5080 |
| sharpe_ratio | -3.2485 |
| sortino_ratio | -0.8799 |
| max_drawdown | 0.6702 |
| cagr | -0.3496 |
| net_avg_win | 51.9164 |
| net_avg_loss | -83.4488 |
| avg_hold_time_bars | 8.9016 |
| exposure | 0.1521 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
