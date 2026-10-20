# EMA Hourly Continuation — DEEP/USDT P20_89

**Symbol:** DEEP/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 503 |
| net_profit_factor | 0.7421 |
| net_win_rate | 0.4990 |
| gross_profit_factor | 1.0076 |
| gross_win_rate | 0.5030 |
| sharpe_ratio | -2.5002 |
| sortino_ratio | -0.8882 |
| max_drawdown | 0.5711 |
| cagr | -0.3414 |
| net_avg_win | 65.2518 |
| net_avg_loss | -87.5803 |
| avg_hold_time_bars | 14.6163 |
| exposure | 0.4163 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
