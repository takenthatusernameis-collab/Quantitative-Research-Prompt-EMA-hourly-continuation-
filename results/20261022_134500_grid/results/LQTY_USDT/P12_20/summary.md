# EMA Hourly Continuation — LQTY/USDT P12_20

**Symbol:** LQTY/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1485 |
| net_profit_factor | 0.3160 |
| net_win_rate | 0.4236 |
| gross_profit_factor | 0.8079 |
| gross_win_rate | 0.4620 |
| sharpe_ratio | -12.0871 |
| sortino_ratio | -6.5827 |
| max_drawdown | 0.9998 |
| cagr | -0.9649 |
| net_avg_win | 7.3428 |
| net_avg_loss | -17.0753 |
| avg_hold_time_bars | 2.6007 |
| exposure | 0.1748 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
