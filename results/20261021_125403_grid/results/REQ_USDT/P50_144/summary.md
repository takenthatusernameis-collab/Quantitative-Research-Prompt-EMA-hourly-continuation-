# EMA Hourly Continuation — REQ/USDT P50_144

**Symbol:** REQ/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 390 |
| net_profit_factor | 0.5630 |
| net_win_rate | 0.4282 |
| gross_profit_factor | 0.8152 |
| gross_win_rate | 0.4308 |
| sharpe_ratio | -4.0997 |
| sortino_ratio | -1.1541 |
| max_drawdown | 0.7538 |
| cagr | -0.4147 |
| net_avg_win | 57.0547 |
| net_avg_loss | -75.8902 |
| avg_hold_time_bars | 13.8436 |
| exposure | 0.2454 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
