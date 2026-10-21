# EMA Hourly Continuation — TRB/USDT P21_50

**Symbol:** TRB/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 506 |
| net_profit_factor | 0.5847 |
| net_win_rate | 0.4387 |
| gross_profit_factor | 0.7784 |
| gross_win_rate | 0.4387 |
| sharpe_ratio | -3.9116 |
| sortino_ratio | -1.2483 |
| max_drawdown | 0.7655 |
| cagr | -0.4372 |
| net_avg_win | 48.5362 |
| net_avg_loss | -64.8938 |
| avg_hold_time_bars | 7.1047 |
| exposure | 0.1627 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
