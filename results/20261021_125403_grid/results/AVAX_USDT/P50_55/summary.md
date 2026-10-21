# EMA Hourly Continuation — AVAX/USDT P50_55

**Symbol:** AVAX/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 88 |
| net_profit_factor | 0.6727 |
| net_win_rate | 0.4886 |
| gross_profit_factor | 0.9619 |
| gross_win_rate | 0.4886 |
| sharpe_ratio | -1.1793 |
| sortino_ratio | -0.1589 |
| max_drawdown | 0.1996 |
| cagr | -0.0703 |
| net_avg_win | 79.9336 |
| net_avg_loss | -113.5480 |
| avg_hold_time_bars | 4.7727 |
| exposure | 0.0191 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
