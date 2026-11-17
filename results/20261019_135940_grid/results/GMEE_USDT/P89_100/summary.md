# EMA Hourly Continuation — GMEE/USDT P89_100

**Symbol:** GMEE/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 551 |
| net_profit_factor | 0.2731 |
| net_win_rate | 0.3575 |
| gross_profit_factor | 0.6668 |
| gross_win_rate | 0.3721 |
| sharpe_ratio | -9.2923 |
| sortino_ratio | -3.1466 |
| max_drawdown | 0.9854 |
| cagr | -0.8138 |
| net_avg_win | 18.7958 |
| net_avg_loss | -38.2935 |
| avg_hold_time_bars | 2.3956 |
| exposure | 0.0600 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
