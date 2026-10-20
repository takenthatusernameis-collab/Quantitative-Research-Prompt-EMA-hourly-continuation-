# EMA Hourly Continuation — EDU/USDT P12_200

**Symbol:** EDU/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 472 |
| net_profit_factor | 0.6590 |
| net_win_rate | 0.4513 |
| gross_profit_factor | 0.8572 |
| gross_win_rate | 0.4619 |
| sharpe_ratio | -2.9743 |
| sortino_ratio | -0.9101 |
| max_drawdown | 0.6788 |
| cagr | -0.3497 |
| net_avg_win | 60.0782 |
| net_avg_loss | -74.9761 |
| avg_hold_time_bars | 33.5911 |
| exposure | 0.7175 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
