# EMA Hourly Continuation — TRAC/USDT P55_144

**Symbol:** TRAC/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 526 |
| net_profit_factor | 0.6660 |
| net_win_rate | 0.4981 |
| gross_profit_factor | 0.9862 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -2.8231 |
| sortino_ratio | -0.9132 |
| max_drawdown | 0.6728 |
| cagr | -0.3521 |
| net_avg_win | 50.5231 |
| net_avg_loss | -75.2820 |
| avg_hold_time_bars | 9.1274 |
| exposure | 0.2182 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
