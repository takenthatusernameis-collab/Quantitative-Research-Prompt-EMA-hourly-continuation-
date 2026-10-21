# EMA Hourly Continuation — IMX/USDT P20_21

**Symbol:** IMX/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 141 |
| net_profit_factor | 0.7284 |
| net_win_rate | 0.4965 |
| gross_profit_factor | 1.0060 |
| gross_win_rate | 0.4965 |
| sharpe_ratio | -1.2539 |
| sortino_ratio | -0.2133 |
| max_drawdown | 0.2732 |
| cagr | -0.0932 |
| net_avg_win | 83.7908 |
| net_avg_loss | -113.4103 |
| avg_hold_time_bars | 4.7305 |
| exposure | 0.0302 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
