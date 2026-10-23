# EMA Hourly Continuation — DODO/USDT P20_200

**Symbol:** DODO/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 471 |
| net_profit_factor | 0.5662 |
| net_win_rate | 0.4352 |
| gross_profit_factor | 0.7945 |
| gross_win_rate | 0.4416 |
| sharpe_ratio | -3.8345 |
| sortino_ratio | -1.1705 |
| max_drawdown | 0.7577 |
| cagr | -0.4212 |
| net_avg_win | 47.6445 |
| net_avg_loss | -64.8486 |
| avg_hold_time_bars | 28.2548 |
| exposure | 0.6022 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
