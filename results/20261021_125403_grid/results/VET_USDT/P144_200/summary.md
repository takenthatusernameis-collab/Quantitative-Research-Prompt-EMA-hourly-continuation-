# EMA Hourly Continuation — VET/USDT P144_200

**Symbol:** VET/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 166 |
| net_profit_factor | 0.7078 |
| net_win_rate | 0.4940 |
| gross_profit_factor | 0.9755 |
| gross_win_rate | 0.4940 |
| sharpe_ratio | -1.4056 |
| sortino_ratio | -0.2599 |
| max_drawdown | 0.2705 |
| cagr | -0.1129 |
| net_avg_win | 76.7684 |
| net_avg_loss | -105.8716 |
| avg_hold_time_bars | 7.7831 |
| exposure | 0.0587 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
