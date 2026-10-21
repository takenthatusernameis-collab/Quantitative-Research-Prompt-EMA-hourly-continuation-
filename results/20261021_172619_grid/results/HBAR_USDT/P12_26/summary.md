# EMA Hourly Continuation — HBAR/USDT P12_26

**Symbol:** HBAR/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 395 |
| net_profit_factor | 0.7120 |
| net_win_rate | 0.5063 |
| gross_profit_factor | 1.0277 |
| gross_win_rate | 0.5063 |
| sharpe_ratio | -2.2049 |
| sortino_ratio | -0.6306 |
| max_drawdown | 0.5183 |
| cagr | -0.2498 |
| net_avg_win | 63.5423 |
| net_avg_loss | -91.5385 |
| avg_hold_time_bars | 5.0861 |
| exposure | 0.0913 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
