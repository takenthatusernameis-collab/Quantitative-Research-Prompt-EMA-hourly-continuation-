# EMA Hourly Continuation — NEAR/USDT P8_55

**Symbol:** NEAR/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 631 |
| net_profit_factor | 0.8505 |
| net_win_rate | 0.5103 |
| gross_profit_factor | 1.0354 |
| gross_win_rate | 0.5103 |
| sharpe_ratio | -1.2538 |
| sortino_ratio | -0.4521 |
| max_drawdown | 0.4202 |
| cagr | -0.1911 |
| net_avg_win | 72.9470 |
| net_avg_loss | -89.3815 |
| avg_hold_time_bars | 16.1458 |
| exposure | 0.4631 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
