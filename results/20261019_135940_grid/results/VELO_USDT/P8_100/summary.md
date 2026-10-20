# EMA Hourly Continuation — VELO/USDT P8_100

**Symbol:** VELO/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 797 |
| net_profit_factor | 0.6997 |
| net_win_rate | 0.4994 |
| gross_profit_factor | 0.9647 |
| gross_win_rate | 0.5006 |
| sharpe_ratio | -2.9244 |
| sortino_ratio | -1.1632 |
| max_drawdown | 0.7771 |
| cagr | -0.4267 |
| net_avg_win | 44.0733 |
| net_avg_loss | -62.8279 |
| avg_hold_time_bars | 16.7327 |
| exposure | 0.6062 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
