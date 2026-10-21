# EMA Hourly Continuation — RAY/USDT P89_144

**Symbol:** RAY/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 271 |
| net_profit_factor | 0.7175 |
| net_win_rate | 0.4871 |
| gross_profit_factor | 0.9203 |
| gross_win_rate | 0.4871 |
| sharpe_ratio | -1.5886 |
| sortino_ratio | -0.3736 |
| max_drawdown | 0.3974 |
| cagr | -0.1580 |
| net_avg_win | 67.4530 |
| net_avg_loss | -89.2818 |
| avg_hold_time_bars | 8.4834 |
| exposure | 0.1045 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
