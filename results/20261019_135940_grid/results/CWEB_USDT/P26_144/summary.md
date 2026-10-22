# EMA Hourly Continuation — CWEB/USDT P26_144

**Symbol:** CWEB/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 337 |
| net_profit_factor | 0.6150 |
| net_win_rate | 0.4481 |
| gross_profit_factor | 0.8587 |
| gross_win_rate | 0.4481 |
| sharpe_ratio | -3.1692 |
| sortino_ratio | -0.8201 |
| max_drawdown | 0.6629 |
| cagr | -0.3254 |
| net_avg_win | 66.4376 |
| net_avg_loss | -87.6938 |
| avg_hold_time_bars | 36.2878 |
| exposure | 0.5559 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
