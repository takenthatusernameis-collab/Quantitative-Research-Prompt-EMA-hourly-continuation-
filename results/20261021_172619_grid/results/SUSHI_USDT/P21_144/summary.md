# EMA Hourly Continuation — SUSHI/USDT P21_144

**Symbol:** SUSHI/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 393 |
| net_profit_factor | 0.8383 |
| net_win_rate | 0.5064 |
| gross_profit_factor | 1.0259 |
| gross_win_rate | 0.5064 |
| sharpe_ratio | -1.1080 |
| sortino_ratio | -0.3139 |
| max_drawdown | 0.3682 |
| cagr | -0.1368 |
| net_avg_win | 80.8013 |
| net_avg_loss | -98.8662 |
| avg_hold_time_bars | 28.9898 |
| exposure | 0.5155 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
