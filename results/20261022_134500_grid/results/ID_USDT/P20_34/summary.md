# EMA Hourly Continuation — ID/USDT P20_34

**Symbol:** ID/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1005 |
| net_profit_factor | 0.4096 |
| net_win_rate | 0.4458 |
| gross_profit_factor | 0.9437 |
| gross_win_rate | 0.4716 |
| sharpe_ratio | -8.3748 |
| sortino_ratio | -3.7539 |
| max_drawdown | 0.9905 |
| cagr | -0.8419 |
| net_avg_win | 15.3355 |
| net_avg_loss | -30.1166 |
| avg_hold_time_bars | 3.7313 |
| exposure | 0.1697 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
