# EMA Hourly Continuation — IOTA/USDT P21_100

**Symbol:** IOTA/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 657 |
| net_profit_factor | 0.5754 |
| net_win_rate | 0.4627 |
| gross_profit_factor | 0.9212 |
| gross_win_rate | 0.4718 |
| sharpe_ratio | -4.5386 |
| sortino_ratio | -1.6258 |
| max_drawdown | 0.8698 |
| cagr | -0.5457 |
| net_avg_win | 38.4299 |
| net_avg_loss | -57.5187 |
| avg_hold_time_bars | 13.5616 |
| exposure | 0.4050 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
