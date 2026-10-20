# EMA Hourly Continuation — FLIP/USDT P12_50

**Symbol:** FLIP/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 703 |
| net_profit_factor | 0.5079 |
| net_win_rate | 0.4168 |
| gross_profit_factor | 0.8756 |
| gross_win_rate | 0.4438 |
| sharpe_ratio | -6.9268 |
| sortino_ratio | -2.5763 |
| max_drawdown | 0.9622 |
| cagr | -0.7256 |
| net_avg_win | 33.8498 |
| net_avg_loss | -47.6327 |
| avg_hold_time_bars | 13.3001 |
| exposure | 0.4250 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
