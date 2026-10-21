# EMA Hourly Continuation — UQC/USDT P21_34

**Symbol:** UQC/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 224 |
| net_profit_factor | 0.3513 |
| net_win_rate | 0.3170 |
| gross_profit_factor | 0.5886 |
| gross_win_rate | 0.3438 |
| sharpe_ratio | -5.0428 |
| sortino_ratio | -1.0677 |
| max_drawdown | 0.7229 |
| cagr | -0.3985 |
| net_avg_win | 55.0982 |
| net_avg_loss | -72.7901 |
| avg_hold_time_bars | 43.6786 |
| exposure | 0.4428 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
