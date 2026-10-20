# EMA Hourly Continuation — LUNA/USDT P12_144

**Symbol:** LUNA/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 646 |
| net_profit_factor | 0.5228 |
| net_win_rate | 0.4350 |
| gross_profit_factor | 0.8466 |
| gross_win_rate | 0.4412 |
| sharpe_ratio | -5.7509 |
| sortino_ratio | -2.0356 |
| max_drawdown | 0.9257 |
| cagr | -0.6411 |
| net_avg_win | 36.0092 |
| net_avg_loss | -53.0300 |
| avg_hold_time_bars | 20.9412 |
| exposure | 0.6149 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
