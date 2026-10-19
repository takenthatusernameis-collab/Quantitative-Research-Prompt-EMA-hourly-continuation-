# EMA Hourly Continuation — MANA/USDT P21_34

**Symbol:** MANA/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1149 |
| net_profit_factor | 0.3566 |
| net_win_rate | 0.4091 |
| gross_profit_factor | 0.8848 |
| gross_win_rate | 0.4343 |
| sharpe_ratio | -11.7306 |
| sortino_ratio | -5.6888 |
| max_drawdown | 0.9994 |
| cagr | -0.9468 |
| net_avg_win | 11.7849 |
| net_avg_loss | -22.8757 |
| avg_hold_time_bars | 2.6023 |
| exposure | 0.1359 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
