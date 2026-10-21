# EMA Hourly Continuation — BIGTIME/USDT P12_20

**Symbol:** BIGTIME/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 412 |
| net_profit_factor | 0.5565 |
| net_win_rate | 0.4393 |
| gross_profit_factor | 0.8047 |
| gross_win_rate | 0.4417 |
| sharpe_ratio | -3.9916 |
| sortino_ratio | -1.1544 |
| max_drawdown | 0.7431 |
| cagr | -0.4128 |
| net_avg_win | 51.2210 |
| net_avg_loss | -72.1205 |
| avg_hold_time_bars | 5.3422 |
| exposure | 0.0996 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
