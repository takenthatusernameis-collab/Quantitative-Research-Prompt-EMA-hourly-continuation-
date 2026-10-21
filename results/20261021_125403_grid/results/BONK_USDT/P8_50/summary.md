# EMA Hourly Continuation — BONK/USDT P8_50

**Symbol:** BONK/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 663 |
| net_profit_factor | 0.9122 |
| net_win_rate | 0.5234 |
| gross_profit_factor | 1.0899 |
| gross_win_rate | 0.5234 |
| sharpe_ratio | -0.7224 |
| sortino_ratio | -0.2680 |
| max_drawdown | 0.4967 |
| cagr | -0.1227 |
| net_avg_win | 83.9194 |
| net_avg_loss | -101.0184 |
| avg_hold_time_bars | 13.4781 |
| exposure | 0.4062 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
