# EMA Hourly Continuation — COTI/USDT P8_21

**Symbol:** COTI/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 520 |
| net_profit_factor | 0.7522 |
| net_win_rate | 0.4942 |
| gross_profit_factor | 0.9877 |
| gross_win_rate | 0.4942 |
| sharpe_ratio | -2.1683 |
| sortino_ratio | -0.7084 |
| max_drawdown | 0.6102 |
| cagr | -0.2774 |
| net_avg_win | 65.8865 |
| net_avg_loss | -85.5893 |
| avg_hold_time_bars | 5.7942 |
| exposure | 0.1370 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
