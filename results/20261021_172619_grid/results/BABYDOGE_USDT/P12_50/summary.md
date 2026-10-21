# EMA Hourly Continuation — BABYDOGE/USDT P12_50

**Symbol:** BABYDOGE/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 63 |
| net_profit_factor | 1.0013 |
| net_win_rate | 0.5238 |
| gross_profit_factor | 1.0894 |
| gross_win_rate | 0.5238 |
| sharpe_ratio | 0.0283 |
| sortino_ratio | 0.0032 |
| max_drawdown | 0.0512 |
| cagr | 0.0002 |
| net_avg_win | 95.8200 |
| net_avg_loss | -105.2640 |
| avg_hold_time_bars | 24.0952 |
| exposure | 0.0687 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
