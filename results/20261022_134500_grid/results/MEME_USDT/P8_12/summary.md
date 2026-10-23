# EMA Hourly Continuation — MEME/USDT P8_12

**Symbol:** MEME/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1794 |
| net_profit_factor | 0.2548 |
| net_win_rate | 0.3746 |
| gross_profit_factor | 0.7605 |
| gross_win_rate | 0.4158 |
| sharpe_ratio | -16.4610 |
| sortino_ratio | -10.0245 |
| max_drawdown | 1.0000 |
| cagr | -0.9946 |
| net_avg_win | 5.0876 |
| net_avg_loss | -11.9597 |
| avg_hold_time_bars | 1.9047 |
| exposure | 0.1553 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
