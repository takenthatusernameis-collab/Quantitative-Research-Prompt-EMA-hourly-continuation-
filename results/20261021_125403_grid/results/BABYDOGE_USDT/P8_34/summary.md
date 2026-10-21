# EMA Hourly Continuation — BABYDOGE/USDT P8_34

**Symbol:** BABYDOGE/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 60 |
| net_profit_factor | 0.7477 |
| net_win_rate | 0.4500 |
| gross_profit_factor | 0.8157 |
| gross_win_rate | 0.4500 |
| sharpe_ratio | -0.6983 |
| sortino_ratio | -0.0762 |
| max_drawdown | 0.1064 |
| cagr | -0.0347 |
| net_avg_win | 93.6733 |
| net_avg_loss | -102.5023 |
| avg_hold_time_bars | 11.1333 |
| exposure | 0.0302 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
