# EMA Hourly Continuation — OP/USDT P12_100

**Symbol:** OP/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 644 |
| net_profit_factor | 0.6070 |
| net_win_rate | 0.4457 |
| gross_profit_factor | 0.8835 |
| gross_win_rate | 0.4503 |
| sharpe_ratio | -4.5624 |
| sortino_ratio | -1.6269 |
| max_drawdown | 0.8643 |
| cagr | -0.5387 |
| net_avg_win | 46.1143 |
| net_avg_loss | -61.0709 |
| avg_hold_time_bars | 19.7873 |
| exposure | 0.5792 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
