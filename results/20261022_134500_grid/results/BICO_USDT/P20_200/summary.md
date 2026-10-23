# EMA Hourly Continuation — BICO/USDT P20_200

**Symbol:** BICO/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 340 |
| net_profit_factor | 0.6494 |
| net_win_rate | 0.4471 |
| gross_profit_factor | 0.8390 |
| gross_win_rate | 0.4529 |
| sharpe_ratio | -2.6415 |
| sortino_ratio | -0.6848 |
| max_drawdown | 0.5847 |
| cagr | -0.2761 |
| net_avg_win | 67.7307 |
| net_avg_loss | -84.3198 |
| avg_hold_time_bars | 41.9647 |
| exposure | 0.6485 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
