# EMA Hourly Continuation — 1INCH/USDT P20_50

**Symbol:** 1INCH/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 572 |
| net_profit_factor | 0.5698 |
| net_win_rate | 0.4406 |
| gross_profit_factor | 0.7965 |
| gross_win_rate | 0.4423 |
| sharpe_ratio | -4.4214 |
| sortino_ratio | -1.5078 |
| max_drawdown | 0.8249 |
| cagr | -0.5001 |
| net_avg_win | 43.3495 |
| net_avg_loss | -59.9094 |
| avg_hold_time_bars | 7.1573 |
| exposure | 0.1861 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
