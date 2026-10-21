# EMA Hourly Continuation — OSMO/USDT P26_144

**Symbol:** OSMO/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 391 |
| net_profit_factor | 0.8303 |
| net_win_rate | 0.5090 |
| gross_profit_factor | 1.0415 |
| gross_win_rate | 0.5090 |
| sharpe_ratio | -1.1775 |
| sortino_ratio | -0.3339 |
| max_drawdown | 0.3676 |
| cagr | -0.1443 |
| net_avg_win | 79.6217 |
| net_avg_loss | -99.3904 |
| avg_hold_time_bars | 26.5269 |
| exposure | 0.4715 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
