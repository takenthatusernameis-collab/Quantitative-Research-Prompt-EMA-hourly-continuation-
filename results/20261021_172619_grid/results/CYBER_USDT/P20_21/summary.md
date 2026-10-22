# EMA Hourly Continuation — CYBER/USDT P20_21

**Symbol:** CYBER/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 228 |
| net_profit_factor | 0.5834 |
| net_win_rate | 0.4693 |
| gross_profit_factor | 0.8930 |
| gross_win_rate | 0.4693 |
| sharpe_ratio | -2.6442 |
| sortino_ratio | -0.5708 |
| max_drawdown | 0.5022 |
| cagr | -0.2331 |
| net_avg_win | 63.6668 |
| net_avg_loss | -96.5049 |
| avg_hold_time_bars | 6.4474 |
| exposure | 0.0668 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
