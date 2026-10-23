# EMA Hourly Continuation — ARKM/USDT P26_50

**Symbol:** ARKM/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 969 |
| net_profit_factor | 0.5712 |
| net_win_rate | 0.4510 |
| gross_profit_factor | 0.9770 |
| gross_win_rate | 0.4654 |
| sharpe_ratio | -6.7950 |
| sortino_ratio | -2.9941 |
| max_drawdown | 0.9761 |
| cagr | -0.7628 |
| net_avg_win | 29.6563 |
| net_avg_loss | -42.6509 |
| avg_hold_time_bars | 3.6646 |
| exposure | 0.1614 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
