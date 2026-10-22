# EMA Hourly Continuation — POKT/USDT P89_200

**Symbol:** POKT/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 310 |
| net_profit_factor | 0.6891 |
| net_win_rate | 0.4516 |
| gross_profit_factor | 0.8633 |
| gross_win_rate | 0.4516 |
| sharpe_ratio | -2.3296 |
| sortino_ratio | -0.5803 |
| max_drawdown | 0.5318 |
| cagr | -0.2347 |
| net_avg_win | 77.6870 |
| net_avg_loss | -92.8476 |
| avg_hold_time_bars | 16.7581 |
| exposure | 0.2351 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
