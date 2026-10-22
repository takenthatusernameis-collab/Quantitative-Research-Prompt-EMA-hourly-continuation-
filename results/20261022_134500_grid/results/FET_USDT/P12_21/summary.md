# EMA Hourly Continuation — FET/USDT P12_21

**Symbol:** FET/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1541 |
| net_profit_factor | 0.3861 |
| net_win_rate | 0.4134 |
| gross_profit_factor | 0.8007 |
| gross_win_rate | 0.4393 |
| sharpe_ratio | -12.4704 |
| sortino_ratio | -6.9501 |
| max_drawdown | 0.9999 |
| cagr | -0.9710 |
| net_avg_win | 9.8706 |
| net_avg_loss | -18.0157 |
| avg_hold_time_bars | 2.0857 |
| exposure | 0.1461 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
