# EMA Hourly Continuation — BTT/USDT P21_55

**Symbol:** BTT/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 965 |
| net_profit_factor | 0.2795 |
| net_win_rate | 0.3326 |
| gross_profit_factor | 0.7011 |
| gross_win_rate | 0.3845 |
| sharpe_ratio | -13.6490 |
| sortino_ratio | -6.2351 |
| max_drawdown | 0.9998 |
| cagr | -0.9637 |
| net_avg_win | 12.0816 |
| net_avg_loss | -21.5462 |
| avg_hold_time_bars | 5.8622 |
| exposure | 0.2571 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
