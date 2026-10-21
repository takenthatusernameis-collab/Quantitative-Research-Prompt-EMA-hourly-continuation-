# EMA Hourly Continuation — AURORA/USDT P21_55

**Symbol:** AURORA/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 455 |
| net_profit_factor | 0.5692 |
| net_win_rate | 0.4484 |
| gross_profit_factor | 0.8240 |
| gross_win_rate | 0.4484 |
| sharpe_ratio | -3.9333 |
| sortino_ratio | -1.1946 |
| max_drawdown | 0.7625 |
| cagr | -0.4261 |
| net_avg_win | 48.6995 |
| net_avg_loss | -69.5419 |
| avg_hold_time_bars | 10.5055 |
| exposure | 0.2173 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
