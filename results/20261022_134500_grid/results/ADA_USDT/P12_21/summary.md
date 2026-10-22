# EMA Hourly Continuation — ADA/USDT P12_21

**Symbol:** ADA/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1487 |
| net_profit_factor | 0.2414 |
| net_win_rate | 0.3900 |
| gross_profit_factor | 0.8746 |
| gross_win_rate | 0.4257 |
| sharpe_ratio | -14.8690 |
| sortino_ratio | -8.2513 |
| max_drawdown | 1.0000 |
| cagr | -0.9873 |
| net_avg_win | 5.4851 |
| net_avg_loss | -14.5327 |
| avg_hold_time_bars | 1.9832 |
| exposure | 0.1340 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
