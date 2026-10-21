# EMA Hourly Continuation — IMX/USDT P21_55

**Symbol:** IMX/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 530 |
| net_profit_factor | 0.7661 |
| net_win_rate | 0.4925 |
| gross_profit_factor | 0.9770 |
| gross_win_rate | 0.4925 |
| sharpe_ratio | -1.9905 |
| sortino_ratio | -0.6544 |
| max_drawdown | 0.5756 |
| cagr | -0.2597 |
| net_avg_win | 66.7201 |
| net_avg_loss | -84.4999 |
| avg_hold_time_bars | 8.3189 |
| exposure | 0.1995 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
