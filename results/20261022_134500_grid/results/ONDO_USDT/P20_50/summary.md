# EMA Hourly Continuation — ONDO/USDT P20_50

**Symbol:** ONDO/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 985 |
| net_profit_factor | 0.5518 |
| net_win_rate | 0.4670 |
| gross_profit_factor | 0.9304 |
| gross_win_rate | 0.4782 |
| sharpe_ratio | -6.2490 |
| sortino_ratio | -2.7561 |
| max_drawdown | 0.9667 |
| cagr | -0.7388 |
| net_avg_win | 25.8467 |
| net_avg_loss | -41.0401 |
| avg_hold_time_bars | 4.4071 |
| exposure | 0.1973 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
