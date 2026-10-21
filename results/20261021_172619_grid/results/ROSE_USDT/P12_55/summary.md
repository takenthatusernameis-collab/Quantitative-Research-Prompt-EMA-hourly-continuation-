# EMA Hourly Continuation — ROSE/USDT P12_55

**Symbol:** ROSE/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 624 |
| net_profit_factor | 0.8015 |
| net_win_rate | 0.4968 |
| gross_profit_factor | 0.9933 |
| gross_win_rate | 0.4968 |
| sharpe_ratio | -1.8536 |
| sortino_ratio | -0.6623 |
| max_drawdown | 0.5872 |
| cagr | -0.2636 |
| net_avg_win | 69.8368 |
| net_avg_loss | -86.0272 |
| avg_hold_time_bars | 12.6330 |
| exposure | 0.3583 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
