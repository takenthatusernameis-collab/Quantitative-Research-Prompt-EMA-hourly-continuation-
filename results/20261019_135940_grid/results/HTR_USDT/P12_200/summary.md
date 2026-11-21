# EMA Hourly Continuation — HTR/USDT P12_200

**Symbol:** HTR/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 502 |
| net_profit_factor | 0.5831 |
| net_win_rate | 0.4064 |
| gross_profit_factor | 0.7956 |
| gross_win_rate | 0.4183 |
| sharpe_ratio | -4.9282 |
| sortino_ratio | -1.5313 |
| max_drawdown | 0.8574 |
| cagr | -0.5329 |
| net_avg_win | 58.4215 |
| net_avg_loss | -68.5889 |
| avg_hold_time_bars | 29.5697 |
| exposure | 0.6747 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
