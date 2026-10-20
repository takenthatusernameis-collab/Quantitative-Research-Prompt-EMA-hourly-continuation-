# EMA Hourly Continuation — BABYDOGE/USDT P34_200

**Symbol:** BABYDOGE/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 50 |
| net_profit_factor | 1.0099 |
| net_win_rate | 0.5200 |
| gross_profit_factor | 1.0725 |
| gross_win_rate | 0.5200 |
| sharpe_ratio | 0.0443 |
| sortino_ratio | 0.0045 |
| max_drawdown | 0.0575 |
| cagr | 0.0010 |
| net_avg_win | 96.8789 |
| net_avg_loss | -103.9217 |
| avg_hold_time_bars | 83.5800 |
| exposure | 0.1891 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
