# EMA Hourly Continuation — GALA/USDT P55_144

**Symbol:** GALA/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 310 |
| net_profit_factor | 0.6947 |
| net_win_rate | 0.4645 |
| gross_profit_factor | 0.8567 |
| gross_win_rate | 0.4645 |
| sharpe_ratio | -1.9119 |
| sortino_ratio | -0.4784 |
| max_drawdown | 0.4519 |
| cagr | -0.1974 |
| net_avg_win | 67.0642 |
| net_avg_loss | -83.7440 |
| avg_hold_time_bars | 20.8903 |
| exposure | 0.2944 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
