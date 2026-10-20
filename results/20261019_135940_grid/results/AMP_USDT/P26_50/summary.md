# EMA Hourly Continuation — AMP/USDT P26_50

**Symbol:** AMP/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1335 |
| net_profit_factor | 0.2892 |
| net_win_rate | 0.3551 |
| gross_profit_factor | 0.6387 |
| gross_win_rate | 0.3820 |
| sharpe_ratio | -14.1053 |
| sortino_ratio | -7.3917 |
| max_drawdown | 0.9999 |
| cagr | -0.9769 |
| net_avg_win | 8.5817 |
| net_avg_loss | -16.3379 |
| avg_hold_time_bars | 3.3468 |
| exposure | 0.2031 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
