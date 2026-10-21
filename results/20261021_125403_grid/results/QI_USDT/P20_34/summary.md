# EMA Hourly Continuation — QI/USDT P20_34

**Symbol:** QI/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 497 |
| net_profit_factor | 0.6455 |
| net_win_rate | 0.4990 |
| gross_profit_factor | 0.9845 |
| gross_win_rate | 0.4990 |
| sharpe_ratio | -3.0122 |
| sortino_ratio | -0.9643 |
| max_drawdown | 0.6773 |
| cagr | -0.3543 |
| net_avg_win | 49.0710 |
| net_avg_loss | -75.7128 |
| avg_hold_time_bars | 4.9859 |
| exposure | 0.1121 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
