# EMA Hourly Continuation — METIS/USDT P21_144

**Symbol:** METIS/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 383 |
| net_profit_factor | 0.7275 |
| net_win_rate | 0.4648 |
| gross_profit_factor | 0.8735 |
| gross_win_rate | 0.4648 |
| sharpe_ratio | -2.0228 |
| sortino_ratio | -0.5622 |
| max_drawdown | 0.4926 |
| cagr | -0.2283 |
| net_avg_win | 71.7664 |
| net_avg_loss | -85.6505 |
| avg_hold_time_bars | 29.2846 |
| exposure | 0.5098 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
