# EMA Hourly Continuation — SAFE/USDT P34_200

**Symbol:** SAFE/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 353 |
| net_profit_factor | 0.7998 |
| net_win_rate | 0.5241 |
| gross_profit_factor | 1.1156 |
| gross_win_rate | 0.5297 |
| sharpe_ratio | -1.3193 |
| sortino_ratio | -0.3505 |
| max_drawdown | 0.3576 |
| cagr | -0.1565 |
| net_avg_win | 74.6675 |
| net_avg_loss | -102.8054 |
| avg_hold_time_bars | 34.1955 |
| exposure | 0.5528 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
