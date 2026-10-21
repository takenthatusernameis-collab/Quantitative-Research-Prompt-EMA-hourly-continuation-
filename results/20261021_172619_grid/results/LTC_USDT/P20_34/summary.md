# EMA Hourly Continuation — LTC/USDT P20_34

**Symbol:** LTC/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 245 |
| net_profit_factor | 0.6138 |
| net_win_rate | 0.4857 |
| gross_profit_factor | 0.9576 |
| gross_win_rate | 0.4857 |
| sharpe_ratio | -2.4365 |
| sortino_ratio | -0.5486 |
| max_drawdown | 0.4884 |
| cagr | -0.2202 |
| net_avg_win | 62.0519 |
| net_avg_loss | -95.4746 |
| avg_hold_time_bars | 4.7796 |
| exposure | 0.0532 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
