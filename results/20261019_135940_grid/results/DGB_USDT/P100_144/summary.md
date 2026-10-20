# EMA Hourly Continuation — DGB/USDT P100_144

**Symbol:** DGB/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 597 |
| net_profit_factor | 0.4599 |
| net_win_rate | 0.4322 |
| gross_profit_factor | 0.8702 |
| gross_win_rate | 0.4422 |
| sharpe_ratio | -6.4691 |
| sortino_ratio | -2.2443 |
| max_drawdown | 0.9408 |
| cagr | -0.6679 |
| net_avg_win | 30.9330 |
| net_avg_loss | -51.1882 |
| avg_hold_time_bars | 3.6583 |
| exposure | 0.0993 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
