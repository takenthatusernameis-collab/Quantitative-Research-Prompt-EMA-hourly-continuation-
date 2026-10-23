# EMA Hourly Continuation — SATS/USDT P8_21

**Symbol:** SATS/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1372 |
| net_profit_factor | 0.4990 |
| net_win_rate | 0.4687 |
| gross_profit_factor | 0.8891 |
| gross_win_rate | 0.4774 |
| sharpe_ratio | -7.3649 |
| sortino_ratio | -3.8176 |
| max_drawdown | 0.9913 |
| cagr | -0.8451 |
| net_avg_win | 15.3504 |
| net_avg_loss | -27.1328 |
| avg_hold_time_bars | 3.6407 |
| exposure | 0.2260 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
