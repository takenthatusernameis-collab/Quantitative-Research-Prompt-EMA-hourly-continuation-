# EMA Hourly Continuation — AVAX/USDT P20_21

**Symbol:** AVAX/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1144 |
| net_profit_factor | 0.1252 |
| net_win_rate | 0.2928 |
| gross_profit_factor | 0.6137 |
| gross_win_rate | 0.3636 |
| sharpe_ratio | -18.0907 |
| sortino_ratio | -9.5610 |
| max_drawdown | 1.0000 |
| cagr | -0.9957 |
| net_avg_win | 4.2704 |
| net_avg_loss | -14.1292 |
| avg_hold_time_bars | 1.5044 |
| exposure | 0.0782 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
