# EMA Hourly Continuation — DIA/USDT P34_100

**Symbol:** DIA/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 472 |
| net_profit_factor | 0.6813 |
| net_win_rate | 0.4640 |
| gross_profit_factor | 0.8781 |
| gross_win_rate | 0.4640 |
| sharpe_ratio | -2.7700 |
| sortino_ratio | -0.8549 |
| max_drawdown | 0.6552 |
| cagr | -0.3251 |
| net_avg_win | 61.4150 |
| net_avg_loss | -78.0252 |
| avg_hold_time_bars | 12.8369 |
| exposure | 0.2742 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
