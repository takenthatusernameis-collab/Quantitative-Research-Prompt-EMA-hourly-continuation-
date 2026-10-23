# EMA Hourly Continuation — ROSE/USDT P34_89

**Symbol:** ROSE/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 704 |
| net_profit_factor | 0.6878 |
| net_win_rate | 0.4915 |
| gross_profit_factor | 1.0590 |
| gross_win_rate | 0.5014 |
| sharpe_ratio | -3.6407 |
| sortino_ratio | -1.3684 |
| max_drawdown | 0.8082 |
| cagr | -0.4761 |
| net_avg_win | 51.1267 |
| net_avg_loss | -71.8370 |
| avg_hold_time_bars | 7.9489 |
| exposure | 0.2544 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
