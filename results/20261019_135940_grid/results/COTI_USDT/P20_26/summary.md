# EMA Hourly Continuation — COTI/USDT P20_26

**Symbol:** COTI/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1246 |
| net_profit_factor | 0.3294 |
| net_win_rate | 0.3876 |
| gross_profit_factor | 0.8131 |
| gross_win_rate | 0.4205 |
| sharpe_ratio | -12.8622 |
| sortino_ratio | -6.5404 |
| max_drawdown | 0.9998 |
| cagr | -0.9658 |
| net_avg_win | 10.1690 |
| net_avg_loss | -19.5407 |
| avg_hold_time_bars | 1.7889 |
| exposure | 0.1013 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
