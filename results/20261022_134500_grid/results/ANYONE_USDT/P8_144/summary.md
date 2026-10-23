# EMA Hourly Continuation — ANYONE/USDT P8_144

**Symbol:** ANYONE/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 435 |
| net_profit_factor | 0.8314 |
| net_win_rate | 0.5011 |
| gross_profit_factor | 1.0313 |
| gross_win_rate | 0.5080 |
| sharpe_ratio | -1.3467 |
| sortino_ratio | -0.4216 |
| max_drawdown | 0.4388 |
| cagr | -0.1808 |
| net_avg_win | 82.0661 |
| net_avg_loss | -99.1595 |
| avg_hold_time_bars | 33.0506 |
| exposure | 0.7265 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
