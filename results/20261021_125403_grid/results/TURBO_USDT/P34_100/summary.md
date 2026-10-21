# EMA Hourly Continuation — TURBO/USDT P34_100

**Symbol:** TURBO/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 381 |
| net_profit_factor | 0.7780 |
| net_win_rate | 0.4882 |
| gross_profit_factor | 0.9573 |
| gross_win_rate | 0.4882 |
| sharpe_ratio | -1.7460 |
| sortino_ratio | -0.5333 |
| max_drawdown | 0.4732 |
| cagr | -0.2178 |
| net_avg_win | 75.7304 |
| net_avg_loss | -92.8421 |
| avg_hold_time_bars | 10.8950 |
| exposure | 0.2264 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
