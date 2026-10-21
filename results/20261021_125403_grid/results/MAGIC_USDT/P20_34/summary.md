# EMA Hourly Continuation — MAGIC/USDT P20_34

**Symbol:** MAGIC/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 483 |
| net_profit_factor | 0.6746 |
| net_win_rate | 0.4886 |
| gross_profit_factor | 0.9712 |
| gross_win_rate | 0.4886 |
| sharpe_ratio | -2.9118 |
| sortino_ratio | -0.9170 |
| max_drawdown | 0.6896 |
| cagr | -0.3435 |
| net_avg_win | 57.3211 |
| net_avg_loss | -81.1827 |
| avg_hold_time_bars | 5.7681 |
| exposure | 0.1266 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
