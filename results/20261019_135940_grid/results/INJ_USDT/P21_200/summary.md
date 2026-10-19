# EMA Hourly Continuation — INJ/USDT P21_200

**Symbol:** INJ/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 334 |
| net_profit_factor | 0.6647 |
| net_win_rate | 0.4641 |
| gross_profit_factor | 0.8922 |
| gross_win_rate | 0.4701 |
| sharpe_ratio | -2.4493 |
| sortino_ratio | -0.6262 |
| max_drawdown | 0.5475 |
| cagr | -0.2598 |
| net_avg_win | 67.8246 |
| net_avg_loss | -88.3550 |
| avg_hold_time_bars | 42.4790 |
| exposure | 0.6449 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
