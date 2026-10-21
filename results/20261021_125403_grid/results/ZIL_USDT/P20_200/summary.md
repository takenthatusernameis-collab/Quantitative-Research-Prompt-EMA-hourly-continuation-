# EMA Hourly Continuation — ZIL/USDT P20_200

**Symbol:** ZIL/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 306 |
| net_profit_factor | 0.8705 |
| net_win_rate | 0.5196 |
| gross_profit_factor | 1.0714 |
| gross_win_rate | 0.5196 |
| sharpe_ratio | -0.7237 |
| sortino_ratio | -0.1817 |
| max_drawdown | 0.2694 |
| cagr | -0.0832 |
| net_avg_win | 82.8460 |
| net_avg_loss | -102.9435 |
| avg_hold_time_bars | 44.6895 |
| exposure | 0.6216 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
