# EMA Hourly Continuation — ONDO/USDT P12_34

**Symbol:** ONDO/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1280 |
| net_profit_factor | 0.5181 |
| net_win_rate | 0.4516 |
| gross_profit_factor | 0.8698 |
| gross_win_rate | 0.4633 |
| sharpe_ratio | -8.1399 |
| sortino_ratio | -4.0857 |
| max_drawdown | 0.9937 |
| cagr | -0.8665 |
| net_avg_win | 18.4812 |
| net_avg_loss | -29.3710 |
| avg_hold_time_bars | 3.9633 |
| exposure | 0.2306 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
