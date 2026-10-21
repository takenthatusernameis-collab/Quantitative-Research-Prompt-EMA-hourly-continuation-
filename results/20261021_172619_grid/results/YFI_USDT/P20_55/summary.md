# EMA Hourly Continuation — YFI/USDT P20_55

**Symbol:** YFI/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 651 |
| net_profit_factor | 0.6154 |
| net_win_rate | 0.4747 |
| gross_profit_factor | 0.9402 |
| gross_win_rate | 0.4747 |
| sharpe_ratio | -4.2064 |
| sortino_ratio | -1.5363 |
| max_drawdown | 0.8346 |
| cagr | -0.5043 |
| net_avg_win | 42.9748 |
| net_avg_loss | -63.0893 |
| avg_hold_time_bars | 7.4132 |
| exposure | 0.2184 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
