# EMA Hourly Continuation — CRO/USDT P55_200

**Symbol:** CRO/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 256 |
| net_profit_factor | 0.7804 |
| net_win_rate | 0.5117 |
| gross_profit_factor | 1.0348 |
| gross_win_rate | 0.5117 |
| sharpe_ratio | -1.1785 |
| sortino_ratio | -0.2708 |
| max_drawdown | 0.3208 |
| cagr | -0.1178 |
| net_avg_win | 73.2327 |
| net_avg_loss | -98.3493 |
| avg_hold_time_bars | 32.8203 |
| exposure | 0.3819 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
