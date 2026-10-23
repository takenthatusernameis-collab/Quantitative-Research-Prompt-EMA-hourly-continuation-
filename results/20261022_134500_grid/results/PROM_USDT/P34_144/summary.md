# EMA Hourly Continuation — PROM/USDT P34_144

**Symbol:** PROM/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 545 |
| net_profit_factor | 0.4198 |
| net_win_rate | 0.3963 |
| gross_profit_factor | 0.7118 |
| gross_win_rate | 0.4202 |
| sharpe_ratio | -6.1433 |
| sortino_ratio | -2.0159 |
| max_drawdown | 0.9199 |
| cagr | -0.6291 |
| net_avg_win | 30.7194 |
| net_avg_loss | -48.0453 |
| avg_hold_time_bars | 15.9725 |
| exposure | 0.3957 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
