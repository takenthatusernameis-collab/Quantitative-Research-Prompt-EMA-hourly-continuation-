# EMA Hourly Continuation — HTX/USDT P12_55

**Symbol:** HTX/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 627 |
| net_profit_factor | 0.4811 |
| net_win_rate | 0.4195 |
| gross_profit_factor | 0.8003 |
| gross_win_rate | 0.4226 |
| sharpe_ratio | -6.7743 |
| sortino_ratio | -2.4385 |
| max_drawdown | 0.9454 |
| cagr | -0.6843 |
| net_avg_win | 33.3302 |
| net_avg_loss | -50.0549 |
| avg_hold_time_bars | 13.9091 |
| exposure | 0.3947 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
