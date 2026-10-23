# EMA Hourly Continuation — SWFTC/USDT P12_26

**Symbol:** SWFTC/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1336 |
| net_profit_factor | 0.2696 |
| net_win_rate | 0.3855 |
| gross_profit_factor | 0.6409 |
| gross_win_rate | 0.4042 |
| sharpe_ratio | -12.9395 |
| sortino_ratio | -6.7042 |
| max_drawdown | 0.9999 |
| cagr | -0.9699 |
| net_avg_win | 7.1644 |
| net_avg_loss | -16.6725 |
| avg_hold_time_bars | 3.1999 |
| exposure | 0.1943 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
