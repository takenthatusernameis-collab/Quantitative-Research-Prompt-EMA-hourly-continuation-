# EMA Hourly Continuation — TRAC/USDT P12_89

**Symbol:** TRAC/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 529 |
| net_profit_factor | 0.8491 |
| net_win_rate | 0.5047 |
| gross_profit_factor | 1.0302 |
| gross_win_rate | 0.5047 |
| sharpe_ratio | -1.2455 |
| sortino_ratio | -0.4107 |
| max_drawdown | 0.4180 |
| cagr | -0.1741 |
| net_avg_win | 80.3733 |
| net_avg_loss | -96.4664 |
| avg_hold_time_bars | 18.2760 |
| exposure | 0.4395 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
