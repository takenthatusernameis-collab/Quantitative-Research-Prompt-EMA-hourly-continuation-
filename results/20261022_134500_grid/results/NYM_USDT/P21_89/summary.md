# EMA Hourly Continuation — NYM/USDT P21_89

**Symbol:** NYM/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 631 |
| net_profit_factor | 0.3524 |
| net_win_rate | 0.3756 |
| gross_profit_factor | 0.6952 |
| gross_win_rate | 0.4073 |
| sharpe_ratio | -8.2668 |
| sortino_ratio | -2.9218 |
| max_drawdown | 0.9788 |
| cagr | -0.7807 |
| net_avg_win | 22.4484 |
| net_avg_loss | -38.3220 |
| avg_hold_time_bars | 13.6086 |
| exposure | 0.3903 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
