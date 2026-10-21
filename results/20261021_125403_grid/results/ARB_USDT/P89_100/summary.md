# EMA Hourly Continuation — ARB/USDT P89_100

**Symbol:** ARB/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 102 |
| net_profit_factor | 0.8511 |
| net_win_rate | 0.5490 |
| gross_profit_factor | 1.2024 |
| gross_win_rate | 0.5490 |
| sharpe_ratio | -0.4623 |
| sortino_ratio | -0.0678 |
| max_drawdown | 0.1348 |
| cagr | -0.0311 |
| net_avg_win | 77.7675 |
| net_avg_loss | -111.2353 |
| avg_hold_time_bars | 6.0686 |
| exposure | 0.0281 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
