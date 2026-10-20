# EMA Hourly Continuation — AIOZ/USDT P12_200

**Symbol:** AIOZ/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 507 |
| net_profit_factor | 0.6440 |
| net_win_rate | 0.4556 |
| gross_profit_factor | 0.8753 |
| gross_win_rate | 0.4615 |
| sharpe_ratio | -3.5518 |
| sortino_ratio | -1.1223 |
| max_drawdown | 0.7662 |
| cagr | -0.4157 |
| net_avg_win | 57.9928 |
| net_avg_loss | -75.3704 |
| avg_hold_time_bars | 30.9191 |
| exposure | 0.7125 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
