# EMA Hourly Continuation — SWFTC/USDT P20_21

**Symbol:** SWFTC/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1131 |
| net_profit_factor | 0.0639 |
| net_win_rate | 0.2476 |
| gross_profit_factor | 0.3332 |
| gross_win_rate | 0.3139 |
| sharpe_ratio | -18.9641 |
| sortino_ratio | -9.9517 |
| max_drawdown | 1.0000 |
| cagr | -0.9967 |
| net_avg_win | 2.4388 |
| net_avg_loss | -12.5533 |
| avg_hold_time_bars | 1.8868 |
| exposure | 0.0970 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
