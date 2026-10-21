# EMA Hourly Continuation — THETA/USDT P34_144

**Symbol:** THETA/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 371 |
| net_profit_factor | 0.7641 |
| net_win_rate | 0.4852 |
| gross_profit_factor | 0.9428 |
| gross_win_rate | 0.4852 |
| sharpe_ratio | -1.6167 |
| sortino_ratio | -0.4444 |
| max_drawdown | 0.4217 |
| cagr | -0.1852 |
| net_avg_win | 72.3513 |
| net_avg_loss | -89.2404 |
| avg_hold_time_bars | 19.8922 |
| exposure | 0.3355 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
