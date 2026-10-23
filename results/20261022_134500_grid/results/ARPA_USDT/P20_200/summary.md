# EMA Hourly Continuation — ARPA/USDT P20_200

**Symbol:** ARPA/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 478 |
| net_profit_factor | 0.5644 |
| net_win_rate | 0.4498 |
| gross_profit_factor | 0.8237 |
| gross_win_rate | 0.4519 |
| sharpe_ratio | -3.9038 |
| sortino_ratio | -1.1927 |
| max_drawdown | 0.7966 |
| cagr | -0.4381 |
| net_avg_win | 46.1794 |
| net_avg_loss | -66.8920 |
| avg_hold_time_bars | 28.1318 |
| exposure | 0.6085 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
