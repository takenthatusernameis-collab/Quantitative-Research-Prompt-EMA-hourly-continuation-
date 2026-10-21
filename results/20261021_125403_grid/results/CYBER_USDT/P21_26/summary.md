# EMA Hourly Continuation — CYBER/USDT P21_26

**Symbol:** CYBER/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 281 |
| net_profit_factor | 0.5739 |
| net_win_rate | 0.4555 |
| gross_profit_factor | 0.8685 |
| gross_win_rate | 0.4626 |
| sharpe_ratio | -3.0261 |
| sortino_ratio | -0.7246 |
| max_drawdown | 0.5790 |
| cagr | -0.2850 |
| net_avg_win | 59.9073 |
| net_avg_loss | -87.3329 |
| avg_hold_time_bars | 6.1317 |
| exposure | 0.0783 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
