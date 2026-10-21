# EMA Hourly Continuation — MINA/USDT P8_50

**Symbol:** MINA/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 677 |
| net_profit_factor | 0.7790 |
| net_win_rate | 0.5007 |
| gross_profit_factor | 1.0061 |
| gross_win_rate | 0.5007 |
| sharpe_ratio | -2.1695 |
| sortino_ratio | -0.8071 |
| max_drawdown | 0.6555 |
| cagr | -0.3121 |
| net_avg_win | 63.3393 |
| net_avg_loss | -81.5483 |
| avg_hold_time_bars | 15.9705 |
| exposure | 0.4915 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
