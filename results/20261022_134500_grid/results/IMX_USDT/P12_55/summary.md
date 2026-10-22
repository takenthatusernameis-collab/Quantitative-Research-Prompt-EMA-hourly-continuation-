# EMA Hourly Continuation — IMX/USDT P12_55

**Symbol:** IMX/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 947 |
| net_profit_factor | 0.6617 |
| net_win_rate | 0.4984 |
| gross_profit_factor | 1.0153 |
| gross_win_rate | 0.5079 |
| sharpe_ratio | -3.8740 |
| sortino_ratio | -1.6766 |
| max_drawdown | 0.8770 |
| cagr | -0.5497 |
| net_avg_win | 35.9080 |
| net_avg_loss | -53.9198 |
| avg_hold_time_bars | 8.9102 |
| exposure | 0.3818 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
