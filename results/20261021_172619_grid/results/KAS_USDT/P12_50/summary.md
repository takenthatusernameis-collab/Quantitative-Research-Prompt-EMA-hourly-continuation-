# EMA Hourly Continuation — KAS/USDT P12_50

**Symbol:** KAS/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 625 |
| net_profit_factor | 0.8740 |
| net_win_rate | 0.5344 |
| gross_profit_factor | 1.1245 |
| gross_win_rate | 0.5344 |
| sharpe_ratio | -0.9136 |
| sortino_ratio | -0.3302 |
| max_drawdown | 0.3635 |
| cagr | -0.1450 |
| net_avg_win | 67.5498 |
| net_avg_loss | -88.7097 |
| avg_hold_time_bars | 10.0208 |
| exposure | 0.2847 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
