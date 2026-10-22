# EMA Hourly Continuation — PYTH/USDT P50_200

**Symbol:** PYTH/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 400 |
| net_profit_factor | 0.6825 |
| net_win_rate | 0.4825 |
| gross_profit_factor | 0.9388 |
| gross_win_rate | 0.4850 |
| sharpe_ratio | -2.4001 |
| sortino_ratio | -0.6769 |
| max_drawdown | 0.5777 |
| cagr | -0.2739 |
| net_avg_win | 61.5119 |
| net_avg_loss | -84.0377 |
| avg_hold_time_bars | 21.1425 |
| exposure | 0.3844 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
