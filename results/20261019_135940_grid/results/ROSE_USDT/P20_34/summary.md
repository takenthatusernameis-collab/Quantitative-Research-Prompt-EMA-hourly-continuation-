# EMA Hourly Continuation — ROSE/USDT P20_34

**Symbol:** ROSE/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1236 |
| net_profit_factor | 0.3930 |
| net_win_rate | 0.4150 |
| gross_profit_factor | 0.8284 |
| gross_win_rate | 0.4337 |
| sharpe_ratio | -10.6011 |
| sortino_ratio | -5.2990 |
| max_drawdown | 0.9987 |
| cagr | -0.9280 |
| net_avg_win | 12.6023 |
| net_avg_loss | -22.7545 |
| avg_hold_time_bars | 2.7371 |
| exposure | 0.1538 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
