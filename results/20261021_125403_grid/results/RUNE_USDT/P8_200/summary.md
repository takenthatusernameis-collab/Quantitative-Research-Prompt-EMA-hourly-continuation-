# EMA Hourly Continuation — RUNE/USDT P8_200

**Symbol:** RUNE/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 264 |
| net_profit_factor | 0.8781 |
| net_win_rate | 0.5114 |
| gross_profit_factor | 1.0393 |
| gross_win_rate | 0.5114 |
| sharpe_ratio | -0.6119 |
| sortino_ratio | -0.1427 |
| max_drawdown | 0.2157 |
| cagr | -0.0658 |
| net_avg_win | 83.8121 |
| net_avg_loss | -99.8876 |
| avg_hold_time_bars | 66.4394 |
| exposure | 0.7973 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
