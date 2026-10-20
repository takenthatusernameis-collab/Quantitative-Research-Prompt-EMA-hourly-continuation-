# EMA Hourly Continuation — CPOOL/USDT P20_34

**Symbol:** CPOOL/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1099 |
| net_profit_factor | 0.5361 |
| net_win_rate | 0.4586 |
| gross_profit_factor | 0.8868 |
| gross_win_rate | 0.4732 |
| sharpe_ratio | -7.5595 |
| sortino_ratio | -3.4915 |
| max_drawdown | 0.9884 |
| cagr | -0.8294 |
| net_avg_win | 22.6579 |
| net_avg_loss | -35.8013 |
| avg_hold_time_bars | 2.8344 |
| exposure | 0.1416 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
