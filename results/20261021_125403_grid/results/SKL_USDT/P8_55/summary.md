# EMA Hourly Continuation — SKL/USDT P8_55

**Symbol:** SKL/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 690 |
| net_profit_factor | 0.8281 |
| net_win_rate | 0.5014 |
| gross_profit_factor | 1.0309 |
| gross_win_rate | 0.5014 |
| sharpe_ratio | -1.8577 |
| sortino_ratio | -0.6987 |
| max_drawdown | 0.6286 |
| cagr | -0.2763 |
| net_avg_win | 77.4428 |
| net_avg_loss | -94.0601 |
| avg_hold_time_bars | 15.6188 |
| exposure | 0.4899 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
