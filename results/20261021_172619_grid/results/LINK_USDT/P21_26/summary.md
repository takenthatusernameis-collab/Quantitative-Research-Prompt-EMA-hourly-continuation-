# EMA Hourly Continuation — LINK/USDT P21_26

**Symbol:** LINK/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 161 |
| net_profit_factor | 0.5271 |
| net_win_rate | 0.4161 |
| gross_profit_factor | 0.7372 |
| gross_win_rate | 0.4161 |
| sharpe_ratio | -2.6685 |
| sortino_ratio | -0.4824 |
| max_drawdown | 0.4562 |
| cagr | -0.2004 |
| net_avg_win | 71.4915 |
| net_avg_loss | -96.6684 |
| avg_hold_time_bars | 5.1615 |
| exposure | 0.0378 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
