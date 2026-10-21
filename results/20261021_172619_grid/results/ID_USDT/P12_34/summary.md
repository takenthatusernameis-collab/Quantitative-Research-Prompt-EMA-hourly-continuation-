# EMA Hourly Continuation — ID/USDT P12_34

**Symbol:** ID/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 710 |
| net_profit_factor | 0.6914 |
| net_win_rate | 0.4859 |
| gross_profit_factor | 0.9790 |
| gross_win_rate | 0.4859 |
| sharpe_ratio | -3.3961 |
| sortino_ratio | -1.2924 |
| max_drawdown | 0.7939 |
| cagr | -0.4468 |
| net_avg_win | 50.3602 |
| net_avg_loss | -68.8444 |
| avg_hold_time_bars | 7.2366 |
| exposure | 0.2325 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
