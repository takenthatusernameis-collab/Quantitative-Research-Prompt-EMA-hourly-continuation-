# EMA Hourly Continuation — PYTH/USDT P55_200

**Symbol:** PYTH/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 405 |
| net_profit_factor | 0.6625 |
| net_win_rate | 0.4765 |
| gross_profit_factor | 0.9190 |
| gross_win_rate | 0.4815 |
| sharpe_ratio | -2.5155 |
| sortino_ratio | -0.7151 |
| max_drawdown | 0.5921 |
| cagr | -0.2856 |
| net_avg_win | 58.0008 |
| net_avg_loss | -79.7032 |
| avg_hold_time_bars | 19.5556 |
| exposure | 0.3600 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
