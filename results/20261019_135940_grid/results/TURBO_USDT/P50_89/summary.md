# EMA Hourly Continuation — TURBO/USDT P50_89

**Symbol:** TURBO/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 586 |
| net_profit_factor | 0.6275 |
| net_win_rate | 0.4846 |
| gross_profit_factor | 1.0138 |
| gross_win_rate | 0.4949 |
| sharpe_ratio | -4.4133 |
| sortino_ratio | -1.6532 |
| max_drawdown | 0.8180 |
| cagr | -0.5470 |
| net_avg_win | 48.0051 |
| net_avg_loss | -71.9393 |
| avg_hold_time_bars | 4.3259 |
| exposure | 0.1383 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
