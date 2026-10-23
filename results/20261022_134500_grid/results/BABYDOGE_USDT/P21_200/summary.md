# EMA Hourly Continuation — BABYDOGE/USDT P21_200

**Symbol:** BABYDOGE/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 59 |
| net_profit_factor | 1.1936 |
| net_win_rate | 0.5593 |
| gross_profit_factor | 1.2558 |
| gross_win_rate | 0.5593 |
| sharpe_ratio | 0.4509 |
| sortino_ratio | 0.0505 |
| max_drawdown | 0.0426 |
| cagr | 0.0208 |
| net_avg_win | 99.6639 |
| net_avg_loss | -105.9758 |
| avg_hold_time_bars | 108.6102 |
| exposure | 0.2900 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
