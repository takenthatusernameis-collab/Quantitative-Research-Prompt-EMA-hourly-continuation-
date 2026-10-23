# EMA Hourly Continuation — TNSR/USDT P8_55

**Symbol:** TNSR/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1005 |
| net_profit_factor | 0.6708 |
| net_win_rate | 0.4667 |
| gross_profit_factor | 0.9650 |
| gross_win_rate | 0.4786 |
| sharpe_ratio | -4.9737 |
| sortino_ratio | -2.2127 |
| max_drawdown | 0.9312 |
| cagr | -0.6527 |
| net_avg_win | 40.4348 |
| net_avg_loss | -52.7418 |
| avg_hold_time_bars | 10.8070 |
| exposure | 0.4915 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
