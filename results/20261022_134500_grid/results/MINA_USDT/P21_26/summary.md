# EMA Hourly Continuation — MINA/USDT P21_26

**Symbol:** MINA/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1222 |
| net_profit_factor | 0.2281 |
| net_win_rate | 0.3887 |
| gross_profit_factor | 0.8448 |
| gross_win_rate | 0.4452 |
| sharpe_ratio | -13.2803 |
| sortino_ratio | -6.7178 |
| max_drawdown | 0.9998 |
| cagr | -0.9689 |
| net_avg_win | 6.2203 |
| net_avg_loss | -17.3400 |
| avg_hold_time_bars | 2.1628 |
| exposure | 0.1201 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
