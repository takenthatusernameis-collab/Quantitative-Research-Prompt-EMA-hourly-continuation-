# EMA Hourly Continuation — CPOOL/USDT P20_21

**Symbol:** CPOOL/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 128 |
| net_profit_factor | 0.7549 |
| net_win_rate | 0.4922 |
| gross_profit_factor | 0.9722 |
| gross_win_rate | 0.4922 |
| sharpe_ratio | -1.0218 |
| sortino_ratio | -0.1653 |
| max_drawdown | 0.2183 |
| cagr | -0.0738 |
| net_avg_win | 85.6832 |
| net_avg_loss | -110.0060 |
| avg_hold_time_bars | 5.3984 |
| exposure | 0.0314 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
