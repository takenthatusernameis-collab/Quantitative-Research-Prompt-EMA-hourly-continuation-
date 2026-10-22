# EMA Hourly Continuation — WOO/USDT P34_100

**Symbol:** WOO/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 431 |
| net_profit_factor | 0.7645 |
| net_win_rate | 0.4849 |
| gross_profit_factor | 0.9608 |
| gross_win_rate | 0.4849 |
| sharpe_ratio | -1.9270 |
| sortino_ratio | -0.5712 |
| max_drawdown | 0.5221 |
| cagr | -0.2315 |
| net_avg_win | 75.1505 |
| net_avg_loss | -92.5425 |
| avg_hold_time_bars | 15.4594 |
| exposure | 0.3029 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
