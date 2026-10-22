# EMA Hourly Continuation — ZPAY/USDT P8_21

**Symbol:** ZPAY/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1121 |
| net_profit_factor | 0.3643 |
| net_win_rate | 0.3336 |
| gross_profit_factor | 0.6156 |
| gross_win_rate | 0.3390 |
| sharpe_ratio | -10.6846 |
| sortino_ratio | -5.0027 |
| max_drawdown | 0.9976 |
| cagr | -0.9081 |
| net_avg_win | 15.2869 |
| net_avg_loss | -21.0081 |
| avg_hold_time_bars | 6.0883 |
| exposure | 0.3088 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
