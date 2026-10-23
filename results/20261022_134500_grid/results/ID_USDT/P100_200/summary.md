# EMA Hourly Continuation — ID/USDT P100_200

**Symbol:** ID/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 352 |
| net_profit_factor | 0.5327 |
| net_win_rate | 0.4489 |
| gross_profit_factor | 0.8494 |
| gross_win_rate | 0.4631 |
| sharpe_ratio | -3.4881 |
| sortino_ratio | -0.9200 |
| max_drawdown | 0.6726 |
| cagr | -0.3577 |
| net_avg_win | 48.5335 |
| net_avg_loss | -74.1998 |
| avg_hold_time_bars | 10.7699 |
| exposure | 0.1716 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
