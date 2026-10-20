# EMA Hourly Continuation — MEME/USDT P8_26

**Symbol:** MEME/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1539 |
| net_profit_factor | 0.5023 |
| net_win_rate | 0.4464 |
| gross_profit_factor | 0.9146 |
| gross_win_rate | 0.4594 |
| sharpe_ratio | -9.0700 |
| sortino_ratio | -5.0051 |
| max_drawdown | 0.9979 |
| cagr | -0.9127 |
| net_avg_win | 14.6578 |
| net_avg_loss | -23.5305 |
| avg_hold_time_bars | 3.8564 |
| exposure | 0.2698 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
