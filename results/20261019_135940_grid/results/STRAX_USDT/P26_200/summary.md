# EMA Hourly Continuation — STRAX/USDT P26_200

**Symbol:** STRAX/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 576 |
| net_profit_factor | 0.5432 |
| net_win_rate | 0.4184 |
| gross_profit_factor | 0.7767 |
| gross_win_rate | 0.4236 |
| sharpe_ratio | -5.2426 |
| sortino_ratio | -1.7724 |
| max_drawdown | 0.8792 |
| cagr | -0.5712 |
| net_avg_win | 43.3784 |
| net_avg_loss | -57.4522 |
| avg_hold_time_bars | 19.5469 |
| exposure | 0.5148 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
