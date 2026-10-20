# EMA Hourly Continuation — BABYDOGE/USDT P50_200

**Symbol:** BABYDOGE/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 46 |
| net_profit_factor | 1.4460 |
| net_win_rate | 0.6087 |
| gross_profit_factor | 1.5408 |
| gross_win_rate | 0.6087 |
| sharpe_ratio | 0.7958 |
| sortino_ratio | 0.0805 |
| max_drawdown | 0.0324 |
| cagr | 0.0335 |
| net_avg_win | 100.4609 |
| net_avg_loss | -108.0727 |
| avg_hold_time_bars | 51.4565 |
| exposure | 0.1071 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
