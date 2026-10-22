# EMA Hourly Continuation — RPL/USDT P8_55

**Symbol:** RPL/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 706 |
| net_profit_factor | 0.8133 |
| net_win_rate | 0.5014 |
| gross_profit_factor | 1.0230 |
| gross_win_rate | 0.5014 |
| sharpe_ratio | -1.9297 |
| sortino_ratio | -0.7321 |
| max_drawdown | 0.5928 |
| cagr | -0.2873 |
| net_avg_win | 70.6909 |
| net_avg_loss | -87.4103 |
| avg_hold_time_bars | 15.7663 |
| exposure | 0.5037 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
