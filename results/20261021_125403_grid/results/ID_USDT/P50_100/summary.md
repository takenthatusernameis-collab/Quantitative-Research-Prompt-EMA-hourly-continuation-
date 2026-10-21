# EMA Hourly Continuation — ID/USDT P50_100

**Symbol:** ID/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 432 |
| net_profit_factor | 0.7196 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 0.9908 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -2.0644 |
| sortino_ratio | -0.6141 |
| max_drawdown | 0.5171 |
| cagr | -0.2447 |
| net_avg_win | 60.2924 |
| net_avg_loss | -83.7825 |
| avg_hold_time_bars | 9.0741 |
| exposure | 0.1774 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
