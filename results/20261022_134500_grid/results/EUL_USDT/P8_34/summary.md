# EMA Hourly Continuation — EUL/USDT P8_34

**Symbol:** EUL/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1252 |
| net_profit_factor | 0.4034 |
| net_win_rate | 0.4321 |
| gross_profit_factor | 0.6776 |
| gross_win_rate | 0.4417 |
| sharpe_ratio | -8.2395 |
| sortino_ratio | -4.0900 |
| max_drawdown | 0.9937 |
| cagr | -0.8656 |
| net_avg_win | 12.4183 |
| net_avg_loss | -23.4228 |
| avg_hold_time_bars | 6.6781 |
| exposure | 0.3800 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
