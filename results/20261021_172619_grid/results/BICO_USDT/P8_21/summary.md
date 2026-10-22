# EMA Hourly Continuation — BICO/USDT P8_21

**Symbol:** BICO/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 786 |
| net_profit_factor | 0.7067 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 0.9804 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -2.9156 |
| sortino_ratio | -1.1728 |
| max_drawdown | 0.7544 |
| cagr | -0.4158 |
| net_avg_win | 45.4107 |
| net_avg_loss | -64.2594 |
| avg_hold_time_bars | 5.6832 |
| exposure | 0.2030 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
