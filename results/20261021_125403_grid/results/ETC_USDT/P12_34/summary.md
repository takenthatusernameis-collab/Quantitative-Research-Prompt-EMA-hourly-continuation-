# EMA Hourly Continuation — ETC/USDT P12_34

**Symbol:** ETC/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 615 |
| net_profit_factor | 0.6489 |
| net_win_rate | 0.4878 |
| gross_profit_factor | 0.9842 |
| gross_win_rate | 0.4878 |
| sharpe_ratio | -3.6057 |
| sortino_ratio | -1.2848 |
| max_drawdown | 0.7740 |
| cagr | -0.4430 |
| net_avg_win | 47.4431 |
| net_avg_loss | -69.6292 |
| avg_hold_time_bars | 6.0081 |
| exposure | 0.1680 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
