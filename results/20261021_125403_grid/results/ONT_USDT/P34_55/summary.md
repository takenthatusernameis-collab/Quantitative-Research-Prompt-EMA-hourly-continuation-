# EMA Hourly Continuation — ONT/USDT P34_55

**Symbol:** ONT/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 351 |
| net_profit_factor | 0.6772 |
| net_win_rate | 0.4957 |
| gross_profit_factor | 0.9953 |
| gross_win_rate | 0.4957 |
| sharpe_ratio | -2.3607 |
| sortino_ratio | -0.6342 |
| max_drawdown | 0.5342 |
| cagr | -0.2524 |
| net_avg_win | 62.6648 |
| net_avg_loss | -90.9720 |
| avg_hold_time_bars | 5.3960 |
| exposure | 0.0857 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
