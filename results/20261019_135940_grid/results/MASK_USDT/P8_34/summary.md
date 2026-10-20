# EMA Hourly Continuation — MASK/USDT P8_34

**Symbol:** MASK/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1295 |
| net_profit_factor | 0.4466 |
| net_win_rate | 0.4463 |
| gross_profit_factor | 0.8808 |
| gross_win_rate | 0.4757 |
| sharpe_ratio | -8.8128 |
| sortino_ratio | -4.4489 |
| max_drawdown | 0.9961 |
| cagr | -0.8904 |
| net_avg_win | 13.9085 |
| net_avg_loss | -25.1051 |
| avg_hold_time_bars | 6.6417 |
| exposure | 0.3910 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
