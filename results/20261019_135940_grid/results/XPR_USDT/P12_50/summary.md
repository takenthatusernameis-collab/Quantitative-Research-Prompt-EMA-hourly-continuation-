# EMA Hourly Continuation — XPR/USDT P12_50

**Symbol:** XPR/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1054 |
| net_profit_factor | 0.4593 |
| net_win_rate | 0.4165 |
| gross_profit_factor | 0.8627 |
| gross_win_rate | 0.4298 |
| sharpe_ratio | -9.3868 |
| sortino_ratio | -4.2726 |
| max_drawdown | 0.9962 |
| cagr | -0.8886 |
| net_avg_win | 19.2718 |
| net_avg_loss | -29.9511 |
| avg_hold_time_bars | 6.4355 |
| exposure | 0.3083 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
