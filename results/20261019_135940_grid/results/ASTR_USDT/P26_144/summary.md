# EMA Hourly Continuation — ASTR/USDT P26_144

**Symbol:** ASTR/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 434 |
| net_profit_factor | 0.6839 |
| net_win_rate | 0.4885 |
| gross_profit_factor | 0.9833 |
| gross_win_rate | 0.4931 |
| sharpe_ratio | -2.4976 |
| sortino_ratio | -0.7318 |
| max_drawdown | 0.6047 |
| cagr | -0.2929 |
| net_avg_win | 59.4789 |
| net_avg_loss | -83.0509 |
| avg_hold_time_bars | 26.5000 |
| exposure | 0.5205 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
