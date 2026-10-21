# EMA Hourly Continuation — JUP/USDT P55_89

**Symbol:** JUP/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 275 |
| net_profit_factor | 0.8081 |
| net_win_rate | 0.5200 |
| gross_profit_factor | 1.0536 |
| gross_win_rate | 0.5200 |
| sharpe_ratio | -0.9783 |
| sortino_ratio | -0.2334 |
| max_drawdown | 0.2965 |
| cagr | -0.1022 |
| net_avg_win | 69.8398 |
| net_avg_loss | -93.6249 |
| avg_hold_time_bars | 6.5273 |
| exposure | 0.0816 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
