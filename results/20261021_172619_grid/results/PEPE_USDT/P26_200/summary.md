# EMA Hourly Continuation — PEPE/USDT P26_200

**Symbol:** PEPE/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 273 |
| net_profit_factor | 0.8089 |
| net_win_rate | 0.4908 |
| gross_profit_factor | 0.9556 |
| gross_win_rate | 0.4908 |
| sharpe_ratio | -1.0821 |
| sortino_ratio | -0.2551 |
| max_drawdown | 0.2840 |
| cagr | -0.1120 |
| net_avg_win | 81.4924 |
| net_avg_loss | -97.1241 |
| avg_hold_time_bars | 46.2125 |
| exposure | 0.5735 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
