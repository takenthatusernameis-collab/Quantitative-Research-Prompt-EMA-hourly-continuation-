# EMA Hourly Continuation — DOGE/USDT P100_144

**Symbol:** DOGE/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 199 |
| net_profit_factor | 0.7238 |
| net_win_rate | 0.5025 |
| gross_profit_factor | 1.0045 |
| gross_win_rate | 0.5025 |
| sharpe_ratio | -1.4097 |
| sortino_ratio | -0.2857 |
| max_drawdown | 0.3028 |
| cagr | -0.1226 |
| net_avg_win | 73.3342 |
| net_avg_loss | -102.3465 |
| avg_hold_time_bars | 6.6533 |
| exposure | 0.0602 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
