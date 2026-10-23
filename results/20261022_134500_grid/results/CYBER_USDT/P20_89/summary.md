# EMA Hourly Continuation — CYBER/USDT P20_89

**Symbol:** CYBER/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 731 |
| net_profit_factor | 0.5694 |
| net_win_rate | 0.4542 |
| gross_profit_factor | 0.8617 |
| gross_win_rate | 0.4651 |
| sharpe_ratio | -4.7438 |
| sortino_ratio | -1.7980 |
| max_drawdown | 0.8910 |
| cagr | -0.5781 |
| net_avg_win | 35.2736 |
| net_avg_loss | -51.5443 |
| avg_hold_time_bars | 11.9343 |
| exposure | 0.3965 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
