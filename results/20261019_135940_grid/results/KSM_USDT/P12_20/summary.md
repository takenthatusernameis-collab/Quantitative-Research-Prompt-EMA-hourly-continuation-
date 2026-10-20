# EMA Hourly Continuation — KSM/USDT P12_20

**Symbol:** KSM/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1501 |
| net_profit_factor | 0.3069 |
| net_win_rate | 0.4071 |
| gross_profit_factor | 0.8851 |
| gross_win_rate | 0.4530 |
| sharpe_ratio | -13.5229 |
| sortino_ratio | -7.4875 |
| max_drawdown | 0.9999 |
| cagr | -0.9783 |
| net_avg_win | 7.2465 |
| net_avg_loss | -16.2101 |
| avg_hold_time_bars | 2.3804 |
| exposure | 0.1624 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
