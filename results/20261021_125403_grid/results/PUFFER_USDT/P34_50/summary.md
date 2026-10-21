# EMA Hourly Continuation — PUFFER/USDT P34_50

**Symbol:** PUFFER/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 217 |
| net_profit_factor | 0.9088 |
| net_win_rate | 0.5530 |
| gross_profit_factor | 1.2284 |
| gross_win_rate | 0.5530 |
| sharpe_ratio | -0.4416 |
| sortino_ratio | -0.1053 |
| max_drawdown | 0.1387 |
| cagr | -0.0500 |
| net_avg_win | 81.6502 |
| net_avg_loss | -111.1524 |
| avg_hold_time_bars | 6.1982 |
| exposure | 0.0761 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
