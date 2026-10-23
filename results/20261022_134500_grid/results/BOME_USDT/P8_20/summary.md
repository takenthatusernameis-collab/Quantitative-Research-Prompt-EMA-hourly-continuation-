# EMA Hourly Continuation — BOME/USDT P8_20

**Symbol:** BOME/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1634 |
| net_profit_factor | 0.4536 |
| net_win_rate | 0.4455 |
| gross_profit_factor | 0.8485 |
| gross_win_rate | 0.4633 |
| sharpe_ratio | -9.9072 |
| sortino_ratio | -5.6157 |
| max_drawdown | 0.9991 |
| cagr | -0.9394 |
| net_avg_win | 11.3921 |
| net_avg_loss | -20.1817 |
| avg_hold_time_bars | 2.7821 |
| exposure | 0.2066 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
