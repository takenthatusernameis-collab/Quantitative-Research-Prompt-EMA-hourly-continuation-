# EMA Hourly Continuation — TRX/USDT P34_55

**Symbol:** TRX/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 738 |
| net_profit_factor | 0.1329 |
| net_win_rate | 0.2954 |
| gross_profit_factor | 0.8415 |
| gross_win_rate | 0.4580 |
| sharpe_ratio | -14.2511 |
| sortino_ratio | -6.0949 |
| max_drawdown | 0.9998 |
| cagr | -0.9646 |
| net_avg_win | 7.0318 |
| net_avg_loss | -22.1743 |
| avg_hold_time_bars | 3.4634 |
| exposure | 0.1162 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
