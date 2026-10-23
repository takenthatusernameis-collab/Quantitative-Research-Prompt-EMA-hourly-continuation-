# EMA Hourly Continuation — DEGEN/USDT P12_20

**Symbol:** DEGEN/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1362 |
| net_profit_factor | 0.4731 |
| net_win_rate | 0.4097 |
| gross_profit_factor | 0.8085 |
| gross_win_rate | 0.4369 |
| sharpe_ratio | -10.7148 |
| sortino_ratio | -5.5898 |
| max_drawdown | 0.9991 |
| cagr | -0.9385 |
| net_avg_win | 16.0741 |
| net_avg_loss | -23.5823 |
| avg_hold_time_bars | 2.6189 |
| exposure | 0.1624 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
