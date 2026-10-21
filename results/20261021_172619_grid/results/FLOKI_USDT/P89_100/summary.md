# EMA Hourly Continuation — FLOKI/USDT P89_100

**Symbol:** FLOKI/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 88 |
| net_profit_factor | 0.9383 |
| net_win_rate | 0.5682 |
| gross_profit_factor | 1.3030 |
| gross_win_rate | 0.5682 |
| sharpe_ratio | -0.1610 |
| sortino_ratio | -0.0220 |
| max_drawdown | 0.1030 |
| cagr | -0.0112 |
| net_avg_win | 84.6003 |
| net_avg_loss | -118.6388 |
| avg_hold_time_bars | 6.3409 |
| exposure | 0.0254 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
