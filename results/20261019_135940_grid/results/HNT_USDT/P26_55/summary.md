# EMA Hourly Continuation — HNT/USDT P26_55

**Symbol:** HNT/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 975 |
| net_profit_factor | 0.4849 |
| net_win_rate | 0.4390 |
| gross_profit_factor | 0.8323 |
| gross_win_rate | 0.4472 |
| sharpe_ratio | -7.4387 |
| sortino_ratio | -3.2848 |
| max_drawdown | 0.9826 |
| cagr | -0.7973 |
| net_avg_win | 21.5971 |
| net_avg_loss | -34.8481 |
| avg_hold_time_bars | 4.1426 |
| exposure | 0.1836 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
