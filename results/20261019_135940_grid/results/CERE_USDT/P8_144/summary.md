# EMA Hourly Continuation — CERE/USDT P8_144

**Symbol:** CERE/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 670 |
| net_profit_factor | 0.4605 |
| net_win_rate | 0.3746 |
| gross_profit_factor | 0.7246 |
| gross_win_rate | 0.3925 |
| sharpe_ratio | -7.7718 |
| sortino_ratio | -2.8283 |
| max_drawdown | 0.9734 |
| cagr | -0.7602 |
| net_avg_win | 33.0677 |
| net_avg_loss | -43.0144 |
| avg_hold_time_bars | 22.5507 |
| exposure | 0.6868 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
