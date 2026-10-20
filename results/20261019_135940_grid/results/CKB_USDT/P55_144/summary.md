# EMA Hourly Continuation — CKB/USDT P55_144

**Symbol:** CKB/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 509 |
| net_profit_factor | 0.5345 |
| net_win_rate | 0.4558 |
| gross_profit_factor | 0.8283 |
| gross_win_rate | 0.4637 |
| sharpe_ratio | -4.1861 |
| sortino_ratio | -1.3294 |
| max_drawdown | 0.8075 |
| cagr | -0.4733 |
| net_avg_win | 39.5966 |
| net_avg_loss | -62.0477 |
| avg_hold_time_bars | 10.2692 |
| exposure | 0.2376 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
