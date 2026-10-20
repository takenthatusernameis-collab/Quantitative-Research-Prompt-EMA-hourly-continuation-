# EMA Hourly Continuation — TURBO/USDT P50_200

**Symbol:** TURBO/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 363 |
| net_profit_factor | 0.7735 |
| net_win_rate | 0.5041 |
| gross_profit_factor | 1.0546 |
| gross_win_rate | 0.5124 |
| sharpe_ratio | -1.7501 |
| sortino_ratio | -0.5196 |
| max_drawdown | 0.4177 |
| cagr | -0.2164 |
| net_avg_win | 74.5570 |
| net_avg_loss | -98.0002 |
| avg_hold_time_bars | 18.3994 |
| exposure | 0.3644 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
