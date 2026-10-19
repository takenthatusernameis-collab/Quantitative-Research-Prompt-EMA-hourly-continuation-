# EMA Hourly Continuation — AERO/USDT P12_200

**Symbol:** AERO/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 307 |
| net_profit_factor | 0.9311 |
| net_win_rate | 0.5375 |
| gross_profit_factor | 1.1655 |
| gross_win_rate | 0.5407 |
| sharpe_ratio | -0.3696 |
| sortino_ratio | -0.0925 |
| max_drawdown | 0.2523 |
| cagr | -0.0467 |
| net_avg_win | 92.6671 |
| net_avg_loss | -115.6471 |
| avg_hold_time_bars | 55.0456 |
| exposure | 0.7681 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
