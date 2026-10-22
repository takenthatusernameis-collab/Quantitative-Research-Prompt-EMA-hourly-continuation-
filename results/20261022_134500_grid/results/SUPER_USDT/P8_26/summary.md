# EMA Hourly Continuation — SUPER/USDT P8_26

**Symbol:** SUPER/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1496 |
| net_profit_factor | 0.5480 |
| net_win_rate | 0.4666 |
| gross_profit_factor | 0.9708 |
| gross_win_rate | 0.4846 |
| sharpe_ratio | -8.2688 |
| sortino_ratio | -4.4898 |
| max_drawdown | 0.9962 |
| cagr | -0.8903 |
| net_avg_win | 17.3007 |
| net_avg_loss | -27.6154 |
| avg_hold_time_bars | 4.0642 |
| exposure | 0.2764 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
