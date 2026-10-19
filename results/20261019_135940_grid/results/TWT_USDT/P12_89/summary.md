# EMA Hourly Continuation — TWT/USDT P12_89

**Symbol:** TWT/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 810 |
| net_profit_factor | 0.5794 |
| net_win_rate | 0.4852 |
| gross_profit_factor | 0.9633 |
| gross_win_rate | 0.4963 |
| sharpe_ratio | -4.5733 |
| sortino_ratio | -1.8309 |
| max_drawdown | 0.9003 |
| cagr | -0.5868 |
| net_avg_win | 31.2471 |
| net_avg_loss | -50.8242 |
| avg_hold_time_bars | 14.6852 |
| exposure | 0.5407 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
