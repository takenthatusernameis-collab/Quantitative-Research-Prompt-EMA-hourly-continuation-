# EMA Hourly Continuation — OP/USDT P55_100

**Symbol:** OP/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 353 |
| net_profit_factor | 0.7467 |
| net_win_rate | 0.4929 |
| gross_profit_factor | 0.9775 |
| gross_win_rate | 0.4929 |
| sharpe_ratio | -1.7543 |
| sortino_ratio | -0.4722 |
| max_drawdown | 0.4439 |
| cagr | -0.1950 |
| net_avg_win | 71.1409 |
| net_avg_loss | -92.6153 |
| avg_hold_time_bars | 7.0567 |
| exposure | 0.1132 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
