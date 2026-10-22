# EMA Hourly Continuation — EWT/USDT P144_200

**Symbol:** EWT/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 163 |
| net_profit_factor | 0.7605 |
| net_win_rate | 0.4969 |
| gross_profit_factor | 0.9806 |
| gross_win_rate | 0.4969 |
| sharpe_ratio | -1.0682 |
| sortino_ratio | -0.1953 |
| max_drawdown | 0.2583 |
| cagr | -0.0865 |
| net_avg_win | 79.7057 |
| net_avg_loss | -103.5311 |
| avg_hold_time_bars | 8.4969 |
| exposure | 0.0630 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
