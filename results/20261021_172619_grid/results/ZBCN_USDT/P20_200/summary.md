# EMA Hourly Continuation — ZBCN/USDT P20_200

**Symbol:** ZBCN/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 383 |
| net_profit_factor | 0.9829 |
| net_win_rate | 0.5326 |
| gross_profit_factor | 1.1252 |
| gross_win_rate | 0.5326 |
| sharpe_ratio | -0.0534 |
| sortino_ratio | -0.0152 |
| max_drawdown | 0.2501 |
| cagr | -0.0143 |
| net_avg_win | 98.3173 |
| net_avg_loss | -113.9951 |
| avg_hold_time_bars | 30.5666 |
| exposure | 0.5416 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
