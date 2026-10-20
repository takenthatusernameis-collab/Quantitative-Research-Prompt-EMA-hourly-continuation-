# EMA Hourly Continuation — ALT/USDT P8_144

**Symbol:** ALT/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 518 |
| net_profit_factor | 0.6629 |
| net_win_rate | 0.4691 |
| gross_profit_factor | 0.8892 |
| gross_win_rate | 0.4749 |
| sharpe_ratio | -2.9717 |
| sortino_ratio | -0.9474 |
| max_drawdown | 0.6940 |
| cagr | -0.3646 |
| net_avg_win | 55.0197 |
| net_avg_loss | -73.3391 |
| avg_hold_time_bars | 30.5251 |
| exposure | 0.7187 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
