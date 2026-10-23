# EMA Hourly Continuation — CARV/USDT P8_21

**Symbol:** CARV/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1164 |
| net_profit_factor | 0.5332 |
| net_win_rate | 0.4536 |
| gross_profit_factor | 1.0503 |
| gross_win_rate | 0.4820 |
| sharpe_ratio | -9.6345 |
| sortino_ratio | -5.1481 |
| max_drawdown | 0.9948 |
| cagr | -0.9224 |
| net_avg_win | 21.5092 |
| net_avg_loss | -33.4920 |
| avg_hold_time_bars | 4.1022 |
| exposure | 0.2687 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
