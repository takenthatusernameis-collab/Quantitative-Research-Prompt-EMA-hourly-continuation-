# EMA Hourly Continuation — AURORA/USDT P12_21

**Symbol:** AURORA/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 353 |
| net_profit_factor | 0.5034 |
| net_win_rate | 0.4334 |
| gross_profit_factor | 0.8454 |
| gross_win_rate | 0.4363 |
| sharpe_ratio | -4.5606 |
| sortino_ratio | -1.2329 |
| max_drawdown | 0.7737 |
| cagr | -0.4376 |
| net_avg_win | 50.6321 |
| net_avg_loss | -76.9504 |
| avg_hold_time_bars | 6.8924 |
| exposure | 0.1106 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
