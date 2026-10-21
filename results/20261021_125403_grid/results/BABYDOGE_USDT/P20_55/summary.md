# EMA Hourly Continuation — BABYDOGE/USDT P20_55

**Symbol:** BABYDOGE/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 37 |
| net_profit_factor | 1.1992 |
| net_win_rate | 0.5676 |
| gross_profit_factor | 1.3015 |
| gross_win_rate | 0.5676 |
| sharpe_ratio | 0.3626 |
| sortino_ratio | 0.0322 |
| max_drawdown | 0.0315 |
| cagr | 0.0132 |
| net_avg_win | 96.7118 |
| net_avg_loss | -105.8477 |
| avg_hold_time_bars | 25.8649 |
| exposure | 0.0433 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
