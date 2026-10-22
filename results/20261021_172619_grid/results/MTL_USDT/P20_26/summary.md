# EMA Hourly Continuation — MTL/USDT P20_26

**Symbol:** MTL/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 394 |
| net_profit_factor | 0.4547 |
| net_win_rate | 0.4467 |
| gross_profit_factor | 0.8256 |
| gross_win_rate | 0.4518 |
| sharpe_ratio | -4.8375 |
| sortino_ratio | -1.3775 |
| max_drawdown | 0.8106 |
| cagr | -0.4765 |
| net_avg_win | 38.1127 |
| net_avg_loss | -67.6780 |
| avg_hold_time_bars | 5.1599 |
| exposure | 0.0920 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
