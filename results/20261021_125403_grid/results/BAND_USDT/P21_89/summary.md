# EMA Hourly Continuation — BAND/USDT P21_89

**Symbol:** BAND/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 525 |
| net_profit_factor | 0.7298 |
| net_win_rate | 0.4819 |
| gross_profit_factor | 0.9538 |
| gross_win_rate | 0.4857 |
| sharpe_ratio | -2.4733 |
| sortino_ratio | -0.8061 |
| max_drawdown | 0.6232 |
| cagr | -0.3100 |
| net_avg_win | 64.9089 |
| net_avg_loss | -82.7230 |
| avg_hold_time_bars | 16.1524 |
| exposure | 0.3837 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
