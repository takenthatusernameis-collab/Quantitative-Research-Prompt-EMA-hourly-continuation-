# EMA Hourly Continuation — MAGIC/USDT P21_144

**Symbol:** MAGIC/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 378 |
| net_profit_factor | 0.8353 |
| net_win_rate | 0.5106 |
| gross_profit_factor | 1.0433 |
| gross_win_rate | 0.5106 |
| sharpe_ratio | -1.1647 |
| sortino_ratio | -0.3242 |
| max_drawdown | 0.4189 |
| cagr | -0.1407 |
| net_avg_win | 83.1900 |
| net_avg_loss | -103.9030 |
| avg_hold_time_bars | 34.7143 |
| exposure | 0.5965 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
