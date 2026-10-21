# EMA Hourly Continuation — XYO/USDT P50_55

**Symbol:** XYO/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 160 |
| net_profit_factor | 0.4246 |
| net_win_rate | 0.3812 |
| gross_profit_factor | 0.6518 |
| gross_win_rate | 0.3812 |
| sharpe_ratio | -3.4953 |
| sortino_ratio | -0.6323 |
| max_drawdown | 0.5317 |
| cagr | -0.2559 |
| net_avg_win | 63.5721 |
| net_avg_loss | -92.2623 |
| avg_hold_time_bars | 6.4625 |
| exposure | 0.0468 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
