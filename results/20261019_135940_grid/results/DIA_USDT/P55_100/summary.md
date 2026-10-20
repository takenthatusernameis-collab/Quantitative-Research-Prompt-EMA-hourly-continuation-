# EMA Hourly Continuation — DIA/USDT P55_100

**Symbol:** DIA/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 661 |
| net_profit_factor | 0.5845 |
| net_win_rate | 0.4781 |
| gross_profit_factor | 0.9968 |
| gross_win_rate | 0.4902 |
| sharpe_ratio | -4.6942 |
| sortino_ratio | -1.6941 |
| max_drawdown | 0.8797 |
| cagr | -0.5595 |
| net_avg_win | 38.8887 |
| net_avg_loss | -60.9403 |
| avg_hold_time_bars | 5.3480 |
| exposure | 0.1600 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
