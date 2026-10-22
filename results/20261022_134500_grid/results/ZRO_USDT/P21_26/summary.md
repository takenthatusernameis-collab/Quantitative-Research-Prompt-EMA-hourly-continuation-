# EMA Hourly Continuation — ZRO/USDT P21_26

**Symbol:** ZRO/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1164 |
| net_profit_factor | 0.2862 |
| net_win_rate | 0.3677 |
| gross_profit_factor | 0.6576 |
| gross_win_rate | 0.3969 |
| sharpe_ratio | -13.6993 |
| sortino_ratio | -6.9582 |
| max_drawdown | 0.9998 |
| cagr | -0.9745 |
| net_avg_win | 9.3682 |
| net_avg_loss | -19.0321 |
| avg_hold_time_bars | 1.8196 |
| exposure | 0.1037 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
