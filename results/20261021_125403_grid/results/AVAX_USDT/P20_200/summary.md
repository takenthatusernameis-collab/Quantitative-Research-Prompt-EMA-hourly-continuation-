# EMA Hourly Continuation — AVAX/USDT P20_200

**Symbol:** AVAX/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 281 |
| net_profit_factor | 0.8499 |
| net_win_rate | 0.5089 |
| gross_profit_factor | 1.0313 |
| gross_win_rate | 0.5089 |
| sharpe_ratio | -0.8309 |
| sortino_ratio | -0.1999 |
| max_drawdown | 0.2583 |
| cagr | -0.0894 |
| net_avg_win | 83.0223 |
| net_avg_loss | -101.2224 |
| avg_hold_time_bars | 48.1246 |
| exposure | 0.6147 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
