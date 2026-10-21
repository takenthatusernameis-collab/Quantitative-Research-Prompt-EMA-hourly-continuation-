# EMA Hourly Continuation — PYTH/USDT P8_200

**Symbol:** PYTH/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 214 |
| net_profit_factor | 1.0817 |
| net_win_rate | 0.5514 |
| gross_profit_factor | 1.2095 |
| gross_win_rate | 0.5514 |
| sharpe_ratio | 0.4083 |
| sortino_ratio | 0.0867 |
| max_drawdown | 0.1792 |
| cagr | 0.0339 |
| net_avg_win | 97.9243 |
| net_avg_loss | -111.2728 |
| avg_hold_time_bars | 86.7477 |
| exposure | 0.8438 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
