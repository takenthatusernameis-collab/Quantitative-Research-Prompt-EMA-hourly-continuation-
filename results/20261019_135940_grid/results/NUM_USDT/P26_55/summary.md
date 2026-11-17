# EMA Hourly Continuation — NUM/USDT P26_55

**Symbol:** NUM/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 929 |
| net_profit_factor | 0.3467 |
| net_win_rate | 0.3423 |
| gross_profit_factor | 0.6807 |
| gross_win_rate | 0.3563 |
| sharpe_ratio | -10.7583 |
| sortino_ratio | -4.6579 |
| max_drawdown | 0.9970 |
| cagr | -0.9003 |
| net_avg_win | 16.6350 |
| net_avg_loss | -24.9744 |
| avg_hold_time_bars | 5.0043 |
| exposure | 0.2113 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
