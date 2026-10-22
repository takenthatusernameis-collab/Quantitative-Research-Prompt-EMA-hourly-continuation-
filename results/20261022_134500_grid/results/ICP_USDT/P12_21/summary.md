# EMA Hourly Continuation — ICP/USDT P12_21

**Symbol:** ICP/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1518 |
| net_profit_factor | 0.2998 |
| net_win_rate | 0.3887 |
| gross_profit_factor | 0.7419 |
| gross_win_rate | 0.4236 |
| sharpe_ratio | -14.3233 |
| sortino_ratio | -7.9945 |
| max_drawdown | 1.0000 |
| cagr | -0.9844 |
| net_avg_win | 7.2559 |
| net_avg_loss | -15.3887 |
| avg_hold_time_bars | 1.8992 |
| exposure | 0.1310 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
