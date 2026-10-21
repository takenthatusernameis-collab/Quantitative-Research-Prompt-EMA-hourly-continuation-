# EMA Hourly Continuation — JTO/USDT P21_34

**Symbol:** JTO/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 366 |
| net_profit_factor | 0.7297 |
| net_win_rate | 0.4863 |
| gross_profit_factor | 0.9732 |
| gross_win_rate | 0.4863 |
| sharpe_ratio | -2.0226 |
| sortino_ratio | -0.5537 |
| max_drawdown | 0.4940 |
| cagr | -0.2236 |
| net_avg_win | 71.3502 |
| net_avg_loss | -92.5778 |
| avg_hold_time_bars | 5.6475 |
| exposure | 0.0940 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
