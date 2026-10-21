# EMA Hourly Continuation — MANA/USDT P8_20

**Symbol:** MANA/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 515 |
| net_profit_factor | 0.7431 |
| net_win_rate | 0.5165 |
| gross_profit_factor | 1.0702 |
| gross_win_rate | 0.5165 |
| sharpe_ratio | -2.0648 |
| sortino_ratio | -0.6759 |
| max_drawdown | 0.5372 |
| cagr | -0.2642 |
| net_avg_win | 58.4074 |
| net_avg_loss | -83.9712 |
| avg_hold_time_bars | 5.4000 |
| exposure | 0.1264 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
