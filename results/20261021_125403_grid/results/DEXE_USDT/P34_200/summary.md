# EMA Hourly Continuation — DEXE/USDT P34_200

**Symbol:** DEXE/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 241 |
| net_profit_factor | 0.8662 |
| net_win_rate | 0.5145 |
| gross_profit_factor | 1.0309 |
| gross_win_rate | 0.5145 |
| sharpe_ratio | -0.6004 |
| sortino_ratio | -0.1336 |
| max_drawdown | 0.2542 |
| cagr | -0.0616 |
| net_avg_win | 77.0122 |
| net_avg_loss | -94.2233 |
| avg_hold_time_bars | 54.8506 |
| exposure | 0.6009 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
