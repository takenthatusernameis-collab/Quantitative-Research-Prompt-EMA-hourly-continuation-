# EMA Hourly Continuation — PEPE/USDT P12_26

**Symbol:** PEPE/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 379 |
| net_profit_factor | 0.7445 |
| net_win_rate | 0.4881 |
| gross_profit_factor | 0.9644 |
| gross_win_rate | 0.4881 |
| sharpe_ratio | -1.9056 |
| sortino_ratio | -0.5309 |
| max_drawdown | 0.4619 |
| cagr | -0.2158 |
| net_avg_win | 71.9690 |
| net_avg_loss | -92.1843 |
| avg_hold_time_bars | 5.2639 |
| exposure | 0.0907 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
