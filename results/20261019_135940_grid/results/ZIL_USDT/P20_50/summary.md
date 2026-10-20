# EMA Hourly Continuation — ZIL/USDT P20_50

**Symbol:** ZIL/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1022 |
| net_profit_factor | 0.4428 |
| net_win_rate | 0.4432 |
| gross_profit_factor | 0.8266 |
| gross_win_rate | 0.4599 |
| sharpe_ratio | -8.0404 |
| sortino_ratio | -3.6456 |
| max_drawdown | 0.9889 |
| cagr | -0.8307 |
| net_avg_win | 17.3389 |
| net_avg_loss | -31.1756 |
| avg_hold_time_bars | 4.5900 |
| exposure | 0.2132 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
