# EMA Hourly Continuation — PUFFER/USDT P89_144

**Symbol:** PUFFER/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 224 |
| net_profit_factor | 0.6454 |
| net_win_rate | 0.4598 |
| gross_profit_factor | 0.8214 |
| gross_win_rate | 0.4598 |
| sharpe_ratio | -2.0958 |
| sortino_ratio | -0.4977 |
| max_drawdown | 0.3748 |
| cagr | -0.2040 |
| net_avg_win | 65.1582 |
| net_avg_loss | -85.9425 |
| avg_hold_time_bars | 9.9241 |
| exposure | 0.1258 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
