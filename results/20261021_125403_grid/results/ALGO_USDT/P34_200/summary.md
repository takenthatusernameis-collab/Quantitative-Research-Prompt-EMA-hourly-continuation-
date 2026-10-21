# EMA Hourly Continuation — ALGO/USDT P34_200

**Symbol:** ALGO/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 281 |
| net_profit_factor | 0.8952 |
| net_win_rate | 0.5196 |
| gross_profit_factor | 1.0757 |
| gross_win_rate | 0.5196 |
| sharpe_ratio | -0.5804 |
| sortino_ratio | -0.1398 |
| max_drawdown | 0.2601 |
| cagr | -0.0647 |
| net_avg_win | 90.4519 |
| net_avg_loss | -109.2787 |
| avg_hold_time_bars | 39.0071 |
| exposure | 0.4982 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
