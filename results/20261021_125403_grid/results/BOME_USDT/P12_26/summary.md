# EMA Hourly Continuation — BOME/USDT P12_26

**Symbol:** BOME/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 450 |
| net_profit_factor | 0.7986 |
| net_win_rate | 0.5067 |
| gross_profit_factor | 1.0233 |
| gross_win_rate | 0.5067 |
| sharpe_ratio | -1.5109 |
| sortino_ratio | -0.4603 |
| max_drawdown | 0.4659 |
| cagr | -0.1915 |
| net_avg_win | 71.9542 |
| net_avg_loss | -92.5328 |
| avg_hold_time_bars | 4.5867 |
| exposure | 0.0938 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
