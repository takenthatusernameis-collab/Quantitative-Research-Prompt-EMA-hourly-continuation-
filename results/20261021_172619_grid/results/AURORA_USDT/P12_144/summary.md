# EMA Hourly Continuation — AURORA/USDT P12_144

**Symbol:** AURORA/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 399 |
| net_profit_factor | 0.7535 |
| net_win_rate | 0.4887 |
| gross_profit_factor | 0.9634 |
| gross_win_rate | 0.4887 |
| sharpe_ratio | -1.8436 |
| sortino_ratio | -0.5245 |
| max_drawdown | 0.4922 |
| cagr | -0.2162 |
| net_avg_win | 71.7301 |
| net_avg_loss | -90.9963 |
| avg_hold_time_bars | 33.5088 |
| exposure | 0.6077 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
