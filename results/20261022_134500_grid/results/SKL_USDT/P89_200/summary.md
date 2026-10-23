# EMA Hourly Continuation — SKL/USDT P89_200

**Symbol:** SKL/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 358 |
| net_profit_factor | 0.7182 |
| net_win_rate | 0.5056 |
| gross_profit_factor | 1.0978 |
| gross_win_rate | 0.5251 |
| sharpe_ratio | -1.9726 |
| sortino_ratio | -0.5319 |
| max_drawdown | 0.5392 |
| cagr | -0.2204 |
| net_avg_win | 65.4382 |
| net_avg_loss | -93.1763 |
| avg_hold_time_bars | 13.1983 |
| exposure | 0.2148 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
