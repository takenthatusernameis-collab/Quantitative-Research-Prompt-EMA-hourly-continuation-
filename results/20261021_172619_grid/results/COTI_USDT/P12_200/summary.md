# EMA Hourly Continuation — COTI/USDT P12_200

**Symbol:** COTI/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 343 |
| net_profit_factor | 0.8848 |
| net_win_rate | 0.5073 |
| gross_profit_factor | 1.0291 |
| gross_win_rate | 0.5073 |
| sharpe_ratio | -0.7059 |
| sortino_ratio | -0.1875 |
| max_drawdown | 0.3287 |
| cagr | -0.0857 |
| net_avg_win | 88.9067 |
| net_avg_loss | -103.4531 |
| avg_hold_time_bars | 46.3353 |
| exposure | 0.7224 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
