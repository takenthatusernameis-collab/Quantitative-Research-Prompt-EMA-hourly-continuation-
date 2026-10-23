# EMA Hourly Continuation — TRADE/USDT P21_89

**Symbol:** TRADE/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 568 |
| net_profit_factor | 0.6046 |
| net_win_rate | 0.4665 |
| gross_profit_factor | 0.8773 |
| gross_win_rate | 0.4701 |
| sharpe_ratio | -3.7009 |
| sortino_ratio | -1.2297 |
| max_drawdown | 0.7867 |
| cagr | -0.4532 |
| net_avg_win | 45.0347 |
| net_avg_loss | -65.1423 |
| avg_hold_time_bars | 14.3345 |
| exposure | 0.3701 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
