# EMA Hourly Continuation — ETHFI/USDT P21_50

**Symbol:** ETHFI/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 478 |
| net_profit_factor | 0.7703 |
| net_win_rate | 0.4812 |
| gross_profit_factor | 0.9628 |
| gross_win_rate | 0.4812 |
| sharpe_ratio | -2.0697 |
| sortino_ratio | -0.6459 |
| max_drawdown | 0.5678 |
| cagr | -0.2576 |
| net_avg_win | 76.7760 |
| net_avg_loss | -92.4385 |
| avg_hold_time_bars | 7.8975 |
| exposure | 0.1716 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
