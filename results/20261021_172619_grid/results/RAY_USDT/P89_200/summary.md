# EMA Hourly Continuation — RAY/USDT P89_200

**Symbol:** RAY/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 275 |
| net_profit_factor | 0.7890 |
| net_win_rate | 0.4982 |
| gross_profit_factor | 0.9739 |
| gross_win_rate | 0.4982 |
| sharpe_ratio | -1.1620 |
| sortino_ratio | -0.2756 |
| max_drawdown | 0.3494 |
| cagr | -0.1201 |
| net_avg_win | 74.9981 |
| net_avg_loss | -94.3619 |
| avg_hold_time_bars | 14.5564 |
| exposure | 0.1820 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
