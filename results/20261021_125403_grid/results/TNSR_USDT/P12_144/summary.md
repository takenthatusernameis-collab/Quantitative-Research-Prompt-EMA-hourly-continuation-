# EMA Hourly Continuation — TNSR/USDT P12_144

**Symbol:** TNSR/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 402 |
| net_profit_factor | 0.7734 |
| net_win_rate | 0.4726 |
| gross_profit_factor | 0.9246 |
| gross_win_rate | 0.4726 |
| sharpe_ratio | -1.8643 |
| sortino_ratio | -0.5294 |
| max_drawdown | 0.5083 |
| cagr | -0.2174 |
| net_avg_win | 82.8626 |
| net_avg_loss | -96.0161 |
| avg_hold_time_bars | 36.3706 |
| exposure | 0.6617 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
