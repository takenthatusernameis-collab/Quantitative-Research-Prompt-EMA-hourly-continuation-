# EMA Hourly Continuation — TFUEL/USDT P34_50

**Symbol:** TFUEL/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 291 |
| net_profit_factor | 0.4302 |
| net_win_rate | 0.4089 |
| gross_profit_factor | 0.6764 |
| gross_win_rate | 0.4089 |
| sharpe_ratio | -4.2523 |
| sortino_ratio | -1.0372 |
| max_drawdown | 0.7027 |
| cagr | -0.3794 |
| net_avg_win | 44.4009 |
| net_avg_loss | -71.4108 |
| avg_hold_time_bars | 6.5086 |
| exposure | 0.0857 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
