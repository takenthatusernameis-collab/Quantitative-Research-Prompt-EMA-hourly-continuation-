# EMA Hourly Continuation — OSMO/USDT P55_144

**Symbol:** OSMO/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 337 |
| net_profit_factor | 0.7271 |
| net_win_rate | 0.4866 |
| gross_profit_factor | 0.9423 |
| gross_win_rate | 0.4866 |
| sharpe_ratio | -1.7987 |
| sortino_ratio | -0.4719 |
| max_drawdown | 0.4357 |
| cagr | -0.1950 |
| net_avg_win | 68.2283 |
| net_avg_loss | -88.9522 |
| avg_hold_time_bars | 16.0950 |
| exposure | 0.2465 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
