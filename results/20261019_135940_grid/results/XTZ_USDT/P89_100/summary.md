# EMA Hourly Continuation — XTZ/USDT P89_100

**Symbol:** XTZ/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 632 |
| net_profit_factor | 0.2216 |
| net_win_rate | 0.3766 |
| gross_profit_factor | 0.8648 |
| gross_win_rate | 0.4668 |
| sharpe_ratio | -9.8560 |
| sortino_ratio | -3.6481 |
| max_drawdown | 0.9906 |
| cagr | -0.8434 |
| net_avg_win | 11.8456 |
| net_avg_loss | -32.2950 |
| avg_hold_time_bars | 2.1693 |
| exposure | 0.0623 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
