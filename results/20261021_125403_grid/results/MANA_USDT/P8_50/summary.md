# EMA Hourly Continuation — MANA/USDT P8_50

**Symbol:** MANA/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 657 |
| net_profit_factor | 0.7552 |
| net_win_rate | 0.4855 |
| gross_profit_factor | 0.9813 |
| gross_win_rate | 0.4855 |
| sharpe_ratio | -2.6322 |
| sortino_ratio | -0.9643 |
| max_drawdown | 0.6842 |
| cagr | -0.3579 |
| net_avg_win | 64.9219 |
| net_avg_loss | -81.1330 |
| avg_hold_time_bars | 14.8113 |
| exposure | 0.4423 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
