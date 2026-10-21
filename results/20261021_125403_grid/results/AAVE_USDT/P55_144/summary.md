# EMA Hourly Continuation — AAVE/USDT P55_144

**Symbol:** AAVE/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 328 |
| net_profit_factor | 0.9531 |
| net_win_rate | 0.5457 |
| gross_profit_factor | 1.1890 |
| gross_win_rate | 0.5457 |
| sharpe_ratio | -0.2179 |
| sortino_ratio | -0.0573 |
| max_drawdown | 0.1867 |
| cagr | -0.0308 |
| net_avg_win | 85.8369 |
| net_avg_loss | -108.1907 |
| avg_hold_time_bars | 16.0122 |
| exposure | 0.2387 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
