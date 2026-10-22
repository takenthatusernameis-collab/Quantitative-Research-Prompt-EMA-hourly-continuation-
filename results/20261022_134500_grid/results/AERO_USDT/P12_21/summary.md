# EMA Hourly Continuation — AERO/USDT P12_21

**Symbol:** AERO/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1396 |
| net_profit_factor | 0.2785 |
| net_win_rate | 0.4097 |
| gross_profit_factor | 0.6287 |
| gross_win_rate | 0.4391 |
| sharpe_ratio | -12.0166 |
| sortino_ratio | -6.3422 |
| max_drawdown | 0.9997 |
| cagr | -0.9622 |
| net_avg_win | 6.7455 |
| net_avg_loss | -16.8153 |
| avg_hold_time_bars | 2.3059 |
| exposure | 0.1463 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
