# EMA Hourly Continuation — BONK/USDT P12_50

**Symbol:** BONK/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 591 |
| net_profit_factor | 0.9270 |
| net_win_rate | 0.5296 |
| gross_profit_factor | 1.1209 |
| gross_win_rate | 0.5296 |
| sharpe_ratio | -0.5876 |
| sortino_ratio | -0.2061 |
| max_drawdown | 0.4397 |
| cagr | -0.0971 |
| net_avg_win | 91.8296 |
| net_avg_loss | -111.5275 |
| avg_hold_time_bars | 11.6853 |
| exposure | 0.3139 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
