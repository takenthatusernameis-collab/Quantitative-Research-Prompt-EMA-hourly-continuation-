# EMA Hourly Continuation — TWT/USDT P8_100

**Symbol:** TWT/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 724 |
| net_profit_factor | 0.5460 |
| net_win_rate | 0.4807 |
| gross_profit_factor | 0.9049 |
| gross_win_rate | 0.4945 |
| sharpe_ratio | -4.4110 |
| sortino_ratio | -1.6620 |
| max_drawdown | 0.8851 |
| cagr | -0.5570 |
| net_avg_win | 30.0860 |
| net_avg_loss | -50.9983 |
| avg_hold_time_bars | 20.2652 |
| exposure | 0.6669 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
