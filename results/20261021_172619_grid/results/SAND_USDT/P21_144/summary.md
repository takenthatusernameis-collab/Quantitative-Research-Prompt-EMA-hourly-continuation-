# EMA Hourly Continuation — SAND/USDT P21_144

**Symbol:** SAND/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 312 |
| net_profit_factor | 0.6797 |
| net_win_rate | 0.4519 |
| gross_profit_factor | 0.8392 |
| gross_win_rate | 0.4519 |
| sharpe_ratio | -2.2517 |
| sortino_ratio | -0.5640 |
| max_drawdown | 0.4907 |
| cagr | -0.2295 |
| net_avg_win | 72.3083 |
| net_avg_loss | -87.7144 |
| avg_hold_time_bars | 41.4551 |
| exposure | 0.5879 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
