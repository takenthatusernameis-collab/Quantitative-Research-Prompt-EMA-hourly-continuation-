# EMA Hourly Continuation — QI/USDT P26_55

**Symbol:** QI/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 522 |
| net_profit_factor | 0.7786 |
| net_win_rate | 0.5307 |
| gross_profit_factor | 1.1269 |
| gross_win_rate | 0.5307 |
| sharpe_ratio | -1.7867 |
| sortino_ratio | -0.5884 |
| max_drawdown | 0.5395 |
| cagr | -0.2353 |
| net_avg_win | 62.4462 |
| net_avg_loss | -90.6745 |
| avg_hold_time_bars | 6.7490 |
| exposure | 0.1594 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
