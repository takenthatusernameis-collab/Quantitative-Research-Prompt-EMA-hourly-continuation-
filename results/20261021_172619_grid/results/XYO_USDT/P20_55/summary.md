# EMA Hourly Continuation — XYO/USDT P20_55

**Symbol:** XYO/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 551 |
| net_profit_factor | 0.6375 |
| net_win_rate | 0.4555 |
| gross_profit_factor | 0.8855 |
| gross_win_rate | 0.4555 |
| sharpe_ratio | -3.8463 |
| sortino_ratio | -1.2850 |
| max_drawdown | 0.7850 |
| cagr | -0.4468 |
| net_avg_win | 54.3246 |
| net_avg_loss | -71.2987 |
| avg_hold_time_bars | 9.0508 |
| exposure | 0.2257 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
