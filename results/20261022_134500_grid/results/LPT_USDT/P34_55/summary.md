# EMA Hourly Continuation — LPT/USDT P34_55

**Symbol:** LPT/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 949 |
| net_profit_factor | 0.3837 |
| net_win_rate | 0.4131 |
| gross_profit_factor | 0.7063 |
| gross_win_rate | 0.4489 |
| sharpe_ratio | -9.0064 |
| sortino_ratio | -3.9399 |
| max_drawdown | 0.9928 |
| cagr | -0.8567 |
| net_avg_win | 15.7615 |
| net_avg_loss | -28.9093 |
| avg_hold_time_bars | 3.4605 |
| exposure | 0.1493 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
