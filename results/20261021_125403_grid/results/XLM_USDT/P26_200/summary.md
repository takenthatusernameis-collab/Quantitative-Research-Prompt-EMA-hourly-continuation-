# EMA Hourly Continuation — XLM/USDT P26_200

**Symbol:** XLM/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 282 |
| net_profit_factor | 0.8238 |
| net_win_rate | 0.5142 |
| gross_profit_factor | 1.0605 |
| gross_win_rate | 0.5142 |
| sharpe_ratio | -0.9760 |
| sortino_ratio | -0.2354 |
| max_drawdown | 0.2867 |
| cagr | -0.1034 |
| net_avg_win | 77.3201 |
| net_avg_loss | -99.3342 |
| avg_hold_time_bars | 44.2518 |
| exposure | 0.5672 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
