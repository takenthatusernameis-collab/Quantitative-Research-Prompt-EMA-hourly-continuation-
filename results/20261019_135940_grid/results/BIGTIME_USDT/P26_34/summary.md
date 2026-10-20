# EMA Hourly Continuation — BIGTIME/USDT P26_34

**Symbol:** BIGTIME/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1047 |
| net_profit_factor | 0.4037 |
| net_win_rate | 0.4327 |
| gross_profit_factor | 0.8947 |
| gross_win_rate | 0.4632 |
| sharpe_ratio | -9.6775 |
| sortino_ratio | -4.4470 |
| max_drawdown | 0.9964 |
| cagr | -0.8921 |
| net_avg_win | 14.8901 |
| net_avg_loss | -28.1294 |
| avg_hold_time_bars | 2.8367 |
| exposure | 0.1344 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
