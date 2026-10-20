# EMA Hourly Continuation — GALA/USDT P50_200

**Symbol:** GALA/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 347 |
| net_profit_factor | 0.6093 |
| net_win_rate | 0.4582 |
| gross_profit_factor | 0.8742 |
| gross_win_rate | 0.4669 |
| sharpe_ratio | -2.7780 |
| sortino_ratio | -0.7285 |
| max_drawdown | 0.5967 |
| cagr | -0.2934 |
| net_avg_win | 57.0752 |
| net_avg_loss | -79.2262 |
| avg_hold_time_bars | 26.9251 |
| exposure | 0.4247 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
