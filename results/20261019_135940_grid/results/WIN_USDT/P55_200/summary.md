# EMA Hourly Continuation — WIN/USDT P55_200

**Symbol:** WIN/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 362 |
| net_profit_factor | 0.4605 |
| net_win_rate | 0.4282 |
| gross_profit_factor | 0.7811 |
| gross_win_rate | 0.4392 |
| sharpe_ratio | -4.3052 |
| sortino_ratio | -1.1675 |
| max_drawdown | 0.7558 |
| cagr | -0.4240 |
| net_avg_win | 41.2974 |
| net_avg_loss | -67.1455 |
| avg_hold_time_bars | 22.2762 |
| exposure | 0.3665 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
