# EMA Hourly Continuation — DOGS/USDT P12_144

**Symbol:** DOGS/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 323 |
| net_profit_factor | 0.8605 |
| net_win_rate | 0.5077 |
| gross_profit_factor | 1.0143 |
| gross_win_rate | 0.5077 |
| sharpe_ratio | -0.8340 |
| sortino_ratio | -0.2322 |
| max_drawdown | 0.2489 |
| cagr | -0.1041 |
| net_avg_win | 79.2144 |
| net_avg_loss | -94.9521 |
| avg_hold_time_bars | 37.8173 |
| exposure | 0.6480 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
