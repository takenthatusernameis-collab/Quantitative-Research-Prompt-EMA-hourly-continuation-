# EMA Hourly Continuation — ASTR/USDT P20_144

**Symbol:** ASTR/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 375 |
| net_profit_factor | 0.8010 |
| net_win_rate | 0.5040 |
| gross_profit_factor | 1.0179 |
| gross_win_rate | 0.5040 |
| sharpe_ratio | -1.3881 |
| sortino_ratio | -0.3838 |
| max_drawdown | 0.4268 |
| cagr | -0.1627 |
| net_avg_win | 76.9135 |
| net_avg_loss | -97.5647 |
| avg_hold_time_bars | 34.3200 |
| exposure | 0.5824 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
