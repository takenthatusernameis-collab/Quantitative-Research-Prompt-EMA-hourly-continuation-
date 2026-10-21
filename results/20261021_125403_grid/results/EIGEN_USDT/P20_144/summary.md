# EMA Hourly Continuation — EIGEN/USDT P20_144

**Symbol:** EIGEN/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 296 |
| net_profit_factor | 0.8733 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 1.0024 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -0.8125 |
| sortino_ratio | -0.2214 |
| max_drawdown | 0.2472 |
| cagr | -0.0998 |
| net_avg_win | 90.3843 |
| net_avg_loss | -103.4929 |
| avg_hold_time_bars | 32.1216 |
| exposure | 0.5291 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
