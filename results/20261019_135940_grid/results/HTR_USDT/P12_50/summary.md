# EMA Hourly Continuation — HTR/USDT P12_50

**Symbol:** HTR/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1097 |
| net_profit_factor | 0.4581 |
| net_win_rate | 0.3920 |
| gross_profit_factor | 0.7094 |
| gross_win_rate | 0.4002 |
| sharpe_ratio | -8.7919 |
| sortino_ratio | -4.0831 |
| max_drawdown | 0.9937 |
| cagr | -0.8651 |
| net_avg_win | 19.5322 |
| net_avg_loss | -27.4866 |
| avg_hold_time_bars | 6.4476 |
| exposure | 0.3215 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
