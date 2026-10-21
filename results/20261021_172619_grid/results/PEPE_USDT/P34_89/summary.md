# EMA Hourly Continuation — PEPE/USDT P34_89

**Symbol:** PEPE/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 370 |
| net_profit_factor | 0.8217 |
| net_win_rate | 0.5054 |
| gross_profit_factor | 1.0219 |
| gross_win_rate | 0.5054 |
| sharpe_ratio | -1.2184 |
| sortino_ratio | -0.3362 |
| max_drawdown | 0.3567 |
| cagr | -0.1443 |
| net_avg_win | 79.8306 |
| net_avg_loss | -99.2729 |
| avg_hold_time_bars | 11.5027 |
| exposure | 0.1935 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
