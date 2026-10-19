# EMA Hourly Continuation — THETA/USDT P12_21

**Symbol:** THETA/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1461 |
| net_profit_factor | 0.3723 |
| net_win_rate | 0.4230 |
| gross_profit_factor | 0.8657 |
| gross_win_rate | 0.4442 |
| sharpe_ratio | -12.2912 |
| sortino_ratio | -6.6862 |
| max_drawdown | 0.9998 |
| cagr | -0.9666 |
| net_avg_win | 9.5975 |
| net_avg_loss | -18.8960 |
| avg_hold_time_bars | 2.2868 |
| exposure | 0.1519 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
