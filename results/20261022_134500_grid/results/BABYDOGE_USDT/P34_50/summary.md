# EMA Hourly Continuation — BABYDOGE/USDT P34_50

**Symbol:** BABYDOGE/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 13 |
| net_profit_factor | 0.7610 |
| net_win_rate | 0.4615 |
| gross_profit_factor | 0.8478 |
| gross_win_rate | 0.4615 |
| sharpe_ratio | -0.2953 |
| sortino_ratio | -0.0151 |
| max_drawdown | 0.0328 |
| cagr | -0.0069 |
| net_avg_win | 92.3983 |
| net_avg_loss | -104.0735 |
| avg_hold_time_bars | 4.4615 |
| exposure | 0.0026 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
