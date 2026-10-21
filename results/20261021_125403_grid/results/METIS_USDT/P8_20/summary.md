# EMA Hourly Continuation — METIS/USDT P8_20

**Symbol:** METIS/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 632 |
| net_profit_factor | 0.7233 |
| net_win_rate | 0.4953 |
| gross_profit_factor | 0.9901 |
| gross_win_rate | 0.4953 |
| sharpe_ratio | -2.7267 |
| sortino_ratio | -0.9826 |
| max_drawdown | 0.6804 |
| cagr | -0.3628 |
| net_avg_win | 56.5710 |
| net_avg_loss | -76.7450 |
| avg_hold_time_bars | 5.1266 |
| exposure | 0.1473 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
