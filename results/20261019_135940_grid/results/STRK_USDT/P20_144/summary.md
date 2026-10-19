# EMA Hourly Continuation — STRK/USDT P20_144

**Symbol:** STRK/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 524 |
| net_profit_factor | 0.7252 |
| net_win_rate | 0.4885 |
| gross_profit_factor | 0.9909 |
| gross_win_rate | 0.4905 |
| sharpe_ratio | -2.6622 |
| sortino_ratio | -0.8523 |
| max_drawdown | 0.6875 |
| cagr | -0.3378 |
| net_avg_win | 66.4768 |
| net_avg_loss | -87.5613 |
| avg_hold_time_bars | 21.6260 |
| exposure | 0.5151 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
