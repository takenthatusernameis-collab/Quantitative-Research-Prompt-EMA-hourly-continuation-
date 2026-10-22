# EMA Hourly Continuation — JUP/USDT P12_55

**Symbol:** JUP/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1043 |
| net_profit_factor | 0.6379 |
| net_win_rate | 0.4756 |
| gross_profit_factor | 0.9614 |
| gross_win_rate | 0.4803 |
| sharpe_ratio | -4.9422 |
| sortino_ratio | -2.2547 |
| max_drawdown | 0.9384 |
| cagr | -0.6560 |
| net_avg_win | 33.0831 |
| net_avg_loss | -47.0264 |
| avg_hold_time_bars | 7.6194 |
| exposure | 0.3612 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
