# EMA Hourly Continuation — ICP/USDT P12_55

**Symbol:** ICP/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1056 |
| net_profit_factor | 0.5353 |
| net_win_rate | 0.4621 |
| gross_profit_factor | 0.8773 |
| gross_win_rate | 0.4735 |
| sharpe_ratio | -6.6181 |
| sortino_ratio | -3.0141 |
| max_drawdown | 0.9766 |
| cagr | -0.7712 |
| net_avg_win | 23.0252 |
| net_avg_loss | -36.9542 |
| avg_hold_time_bars | 7.3939 |
| exposure | 0.3549 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
