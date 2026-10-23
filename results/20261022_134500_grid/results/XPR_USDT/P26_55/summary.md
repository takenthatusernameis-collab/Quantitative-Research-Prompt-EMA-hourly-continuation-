# EMA Hourly Continuation — XPR/USDT P26_55

**Symbol:** XPR/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 818 |
| net_profit_factor | 0.3444 |
| net_win_rate | 0.3949 |
| gross_profit_factor | 0.7115 |
| gross_win_rate | 0.4120 |
| sharpe_ratio | -9.8543 |
| sortino_ratio | -4.0000 |
| max_drawdown | 0.9953 |
| cagr | -0.8792 |
| net_avg_win | 16.1828 |
| net_avg_loss | -30.6617 |
| avg_hold_time_bars | 5.0440 |
| exposure | 0.1875 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
