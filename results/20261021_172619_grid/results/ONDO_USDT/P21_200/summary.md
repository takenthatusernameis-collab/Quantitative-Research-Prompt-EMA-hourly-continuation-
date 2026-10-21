# EMA Hourly Continuation — ONDO/USDT P21_200

**Symbol:** ONDO/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 311 |
| net_profit_factor | 0.9292 |
| net_win_rate | 0.5209 |
| gross_profit_factor | 1.0852 |
| gross_win_rate | 0.5209 |
| sharpe_ratio | -0.3747 |
| sortino_ratio | -0.0951 |
| max_drawdown | 0.2660 |
| cagr | -0.0467 |
| net_avg_win | 91.7965 |
| net_avg_loss | -107.4049 |
| avg_hold_time_bars | 39.3537 |
| exposure | 0.5563 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
