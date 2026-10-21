# EMA Hourly Continuation — IMX/USDT P12_89

**Symbol:** IMX/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 528 |
| net_profit_factor | 0.8651 |
| net_win_rate | 0.5114 |
| gross_profit_factor | 1.0314 |
| gross_win_rate | 0.5114 |
| sharpe_ratio | -0.9328 |
| sortino_ratio | -0.3071 |
| max_drawdown | 0.3352 |
| cagr | -0.1354 |
| net_avg_win | 72.9742 |
| net_avg_loss | -88.2787 |
| avg_hold_time_bars | 20.8864 |
| exposure | 0.4990 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
