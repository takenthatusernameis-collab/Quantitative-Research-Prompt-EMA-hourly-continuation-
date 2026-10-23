# EMA Hourly Continuation — PUFFER/USDT P8_144

**Symbol:** PUFFER/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 425 |
| net_profit_factor | 0.7915 |
| net_win_rate | 0.5129 |
| gross_profit_factor | 1.0396 |
| gross_win_rate | 0.5129 |
| sharpe_ratio | -1.5799 |
| sortino_ratio | -0.5154 |
| max_drawdown | 0.4243 |
| cagr | -0.2178 |
| net_avg_win | 68.0381 |
| net_avg_loss | -90.5322 |
| avg_hold_time_bars | 30.2376 |
| exposure | 0.7272 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
