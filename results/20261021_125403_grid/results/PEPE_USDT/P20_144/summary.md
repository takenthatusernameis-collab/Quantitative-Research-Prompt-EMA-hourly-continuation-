# EMA Hourly Continuation — PEPE/USDT P20_144

**Symbol:** PEPE/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 289 |
| net_profit_factor | 0.7915 |
| net_win_rate | 0.4913 |
| gross_profit_factor | 0.9509 |
| gross_win_rate | 0.4913 |
| sharpe_ratio | -1.1844 |
| sortino_ratio | -0.2875 |
| max_drawdown | 0.2844 |
| cagr | -0.1248 |
| net_avg_win | 76.0518 |
| net_avg_loss | -92.8116 |
| avg_hold_time_bars | 44.9723 |
| exposure | 0.5908 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
