# EMA Hourly Continuation — COMP/USDT P21_55

**Symbol:** COMP/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 586 |
| net_profit_factor | 0.6499 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 0.9276 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -2.8030 |
| sortino_ratio | -0.9730 |
| max_drawdown | 0.7159 |
| cagr | -0.3600 |
| net_avg_win | 42.7008 |
| net_avg_loss | -65.7019 |
| avg_hold_time_bars | 8.7526 |
| exposure | 0.2331 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
