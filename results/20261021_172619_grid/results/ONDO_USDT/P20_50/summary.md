# EMA Hourly Continuation — ONDO/USDT P20_50

**Symbol:** ONDO/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 437 |
| net_profit_factor | 0.8169 |
| net_win_rate | 0.5103 |
| gross_profit_factor | 1.0480 |
| gross_win_rate | 0.5103 |
| sharpe_ratio | -1.3881 |
| sortino_ratio | -0.4171 |
| max_drawdown | 0.4582 |
| cagr | -0.1750 |
| net_avg_win | 76.6515 |
| net_avg_loss | -97.7773 |
| avg_hold_time_bars | 7.8535 |
| exposure | 0.1560 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
