# EMA Hourly Continuation — THETA/USDT P21_34

**Symbol:** THETA/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1101 |
| net_profit_factor | 0.3331 |
| net_win_rate | 0.3896 |
| gross_profit_factor | 0.7502 |
| gross_win_rate | 0.4160 |
| sharpe_ratio | -11.5377 |
| sortino_ratio | -5.4645 |
| max_drawdown | 0.9991 |
| cagr | -0.9391 |
| net_avg_win | 11.6343 |
| net_avg_loss | -22.2950 |
| avg_hold_time_bars | 2.4196 |
| exposure | 0.1211 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
