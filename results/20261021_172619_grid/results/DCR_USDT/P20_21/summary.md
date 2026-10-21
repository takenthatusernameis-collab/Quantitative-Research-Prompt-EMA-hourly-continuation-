# EMA Hourly Continuation — DCR/USDT P20_21

**Symbol:** DCR/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 269 |
| net_profit_factor | 0.5797 |
| net_win_rate | 0.4870 |
| gross_profit_factor | 0.9845 |
| gross_win_rate | 0.4907 |
| sharpe_ratio | -2.7896 |
| sortino_ratio | -0.6570 |
| max_drawdown | 0.5617 |
| cagr | -0.2613 |
| net_avg_win | 56.2527 |
| net_avg_loss | -92.1093 |
| avg_hold_time_bars | 4.4089 |
| exposure | 0.0537 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
