# EMA Hourly Continuation — GRAM/USDT P34_144

**Symbol:** GRAM/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 579 |
| net_profit_factor | 0.4208 |
| net_win_rate | 0.4404 |
| gross_profit_factor | 0.8011 |
| gross_win_rate | 0.4542 |
| sharpe_ratio | -5.7238 |
| sortino_ratio | -1.9303 |
| max_drawdown | 0.9162 |
| cagr | -0.6150 |
| net_avg_win | 25.8983 |
| net_avg_loss | -48.4392 |
| avg_hold_time_bars | 14.2729 |
| exposure | 0.3756 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
