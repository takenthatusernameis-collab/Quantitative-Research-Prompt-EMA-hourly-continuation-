# EMA Hourly Continuation — ENJ/USDT P8_200

**Symbol:** ENJ/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 257 |
| net_profit_factor | 0.9415 |
| net_win_rate | 0.5253 |
| gross_profit_factor | 1.0903 |
| gross_win_rate | 0.5253 |
| sharpe_ratio | -0.2504 |
| sortino_ratio | -0.0576 |
| max_drawdown | 0.2142 |
| cagr | -0.0299 |
| net_avg_win | 87.9701 |
| net_avg_loss | -103.3931 |
| avg_hold_time_bars | 72.1556 |
| exposure | 0.8391 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
