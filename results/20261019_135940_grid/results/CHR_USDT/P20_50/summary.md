# EMA Hourly Continuation — CHR/USDT P20_50

**Symbol:** CHR/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 991 |
| net_profit_factor | 0.5119 |
| net_win_rate | 0.4410 |
| gross_profit_factor | 0.8894 |
| gross_win_rate | 0.4531 |
| sharpe_ratio | -6.9131 |
| sortino_ratio | -3.0595 |
| max_drawdown | 0.9768 |
| cagr | -0.7721 |
| net_avg_win | 23.4194 |
| net_avg_loss | -36.0911 |
| avg_hold_time_bars | 5.2119 |
| exposure | 0.2337 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
