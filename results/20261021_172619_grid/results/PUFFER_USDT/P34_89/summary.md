# EMA Hourly Continuation — PUFFER/USDT P34_89

**Symbol:** PUFFER/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 351 |
| net_profit_factor | 0.9721 |
| net_win_rate | 0.5470 |
| gross_profit_factor | 1.1982 |
| gross_win_rate | 0.5470 |
| sharpe_ratio | -0.1288 |
| sortino_ratio | -0.0391 |
| max_drawdown | 0.1477 |
| cagr | -0.0253 |
| net_avg_win | 91.4361 |
| net_avg_loss | -113.5850 |
| avg_hold_time_bars | 11.3362 |
| exposure | 0.2252 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
