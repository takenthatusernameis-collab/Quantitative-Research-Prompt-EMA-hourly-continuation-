# EMA Hourly Continuation — XPR/USDT P21_144

**Symbol:** XPR/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 531 |
| net_profit_factor | 0.5088 |
| net_win_rate | 0.4595 |
| gross_profit_factor | 0.7928 |
| gross_win_rate | 0.4595 |
| sharpe_ratio | -4.2523 |
| sortino_ratio | -1.3772 |
| max_drawdown | 0.8174 |
| cagr | -0.4834 |
| net_avg_win | 34.3658 |
| net_avg_loss | -57.4269 |
| avg_hold_time_bars | 19.6497 |
| exposure | 0.4743 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
