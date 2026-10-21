# EMA Hourly Continuation — ADA/USDT P50_200

**Symbol:** ADA/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 272 |
| net_profit_factor | 0.8392 |
| net_win_rate | 0.5184 |
| gross_profit_factor | 1.0561 |
| gross_win_rate | 0.5184 |
| sharpe_ratio | -0.8424 |
| sortino_ratio | -0.1994 |
| max_drawdown | 0.2533 |
| cagr | -0.0893 |
| net_avg_win | 77.4723 |
| net_avg_loss | -99.3634 |
| avg_hold_time_bars | 29.2463 |
| exposure | 0.3616 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
