# EMA Hourly Continuation — BSV/USDT P34_89

**Symbol:** BSV/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 764 |
| net_profit_factor | 0.4690 |
| net_win_rate | 0.4319 |
| gross_profit_factor | 0.8114 |
| gross_win_rate | 0.4437 |
| sharpe_ratio | -6.7387 |
| sortino_ratio | -2.6277 |
| max_drawdown | 0.9603 |
| cagr | -0.7200 |
| net_avg_win | 25.6660 |
| net_avg_loss | -41.6148 |
| avg_hold_time_bars | 7.6440 |
| exposure | 0.2655 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
