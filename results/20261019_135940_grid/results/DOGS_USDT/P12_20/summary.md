# EMA Hourly Continuation — DOGS/USDT P12_20

**Symbol:** DOGS/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1335 |
| net_profit_factor | 0.3284 |
| net_win_rate | 0.4060 |
| gross_profit_factor | 0.7030 |
| gross_win_rate | 0.4292 |
| sharpe_ratio | -13.2032 |
| sortino_ratio | -7.3879 |
| max_drawdown | 0.9997 |
| cagr | -0.9779 |
| net_avg_win | 9.0195 |
| net_avg_loss | -18.7715 |
| avg_hold_time_bars | 1.9034 |
| exposure | 0.1348 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
