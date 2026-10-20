# EMA Hourly Continuation — SSV/USDT P12_55

**Symbol:** SSV/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1061 |
| net_profit_factor | 0.6002 |
| net_win_rate | 0.4486 |
| gross_profit_factor | 0.9059 |
| gross_win_rate | 0.4552 |
| sharpe_ratio | -6.3118 |
| sortino_ratio | -2.8882 |
| max_drawdown | 0.9730 |
| cagr | -0.7492 |
| net_avg_win | 30.5799 |
| net_avg_loss | -41.4541 |
| avg_hold_time_bars | 8.3572 |
| exposure | 0.4012 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
