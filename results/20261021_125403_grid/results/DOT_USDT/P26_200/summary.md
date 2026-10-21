# EMA Hourly Continuation — DOT/USDT P26_200

**Symbol:** DOT/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 274 |
| net_profit_factor | 0.8678 |
| net_win_rate | 0.5146 |
| gross_profit_factor | 1.0536 |
| gross_win_rate | 0.5146 |
| sharpe_ratio | -0.7100 |
| sortino_ratio | -0.1688 |
| max_drawdown | 0.2616 |
| cagr | -0.0770 |
| net_avg_win | 84.7979 |
| net_avg_loss | -103.5962 |
| avg_hold_time_bars | 48.3504 |
| exposure | 0.6022 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
