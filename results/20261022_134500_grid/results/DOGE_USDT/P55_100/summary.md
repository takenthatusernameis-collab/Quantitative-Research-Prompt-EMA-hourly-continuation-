# EMA Hourly Continuation — DOGE/USDT P55_100

**Symbol:** DOGE/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 597 |
| net_profit_factor | 0.4484 |
| net_win_rate | 0.4556 |
| gross_profit_factor | 0.8537 |
| gross_win_rate | 0.4757 |
| sharpe_ratio | -6.0389 |
| sortino_ratio | -2.0811 |
| max_drawdown | 0.9270 |
| cagr | -0.6465 |
| net_avg_win | 27.6961 |
| net_avg_loss | -51.6889 |
| avg_hold_time_bars | 5.6868 |
| exposure | 0.1543 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
