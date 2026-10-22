# EMA Hourly Continuation — EWT/USDT P26_144

**Symbol:** EWT/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 416 |
| net_profit_factor | 0.6941 |
| net_win_rate | 0.4663 |
| gross_profit_factor | 0.8408 |
| gross_win_rate | 0.4663 |
| sharpe_ratio | -2.1246 |
| sortino_ratio | -0.6150 |
| max_drawdown | 0.5624 |
| cagr | -0.2467 |
| net_avg_win | 59.5523 |
| net_avg_loss | -74.9724 |
| avg_hold_time_bars | 19.3654 |
| exposure | 0.3662 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
