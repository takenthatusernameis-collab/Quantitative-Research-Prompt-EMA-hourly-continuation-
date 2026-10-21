# EMA Hourly Continuation — ALGO/USDT P26_200

**Symbol:** ALGO/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 283 |
| net_profit_factor | 0.9555 |
| net_win_rate | 0.5336 |
| gross_profit_factor | 1.1279 |
| gross_win_rate | 0.5336 |
| sharpe_ratio | -0.1934 |
| sortino_ratio | -0.0469 |
| max_drawdown | 0.1488 |
| cagr | -0.0258 |
| net_avg_win | 90.4709 |
| net_avg_loss | -108.3104 |
| avg_hold_time_bars | 45.5371 |
| exposure | 0.5858 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
