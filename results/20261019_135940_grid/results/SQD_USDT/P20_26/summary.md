# EMA Hourly Continuation — SQD/USDT P20_26

**Symbol:** SQD/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1133 |
| net_profit_factor | 0.4292 |
| net_win_rate | 0.4051 |
| gross_profit_factor | 0.9389 |
| gross_win_rate | 0.4369 |
| sharpe_ratio | -11.2102 |
| sortino_ratio | -5.4217 |
| max_drawdown | 0.9990 |
| cagr | -0.9412 |
| net_avg_win | 16.3671 |
| net_avg_loss | -25.9677 |
| avg_hold_time_bars | 2.1915 |
| exposure | 0.1167 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
