# EMA Hourly Continuation — POPCAT/USDT P12_55

**Symbol:** POPCAT/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 548 |
| net_profit_factor | 0.7280 |
| net_win_rate | 0.4672 |
| gross_profit_factor | 0.8702 |
| gross_win_rate | 0.4672 |
| sharpe_ratio | -2.5882 |
| sortino_ratio | -0.9282 |
| max_drawdown | 0.6052 |
| cagr | -0.3484 |
| net_avg_win | 63.1201 |
| net_avg_loss | -76.0141 |
| avg_hold_time_bars | 11.4635 |
| exposure | 0.3319 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
