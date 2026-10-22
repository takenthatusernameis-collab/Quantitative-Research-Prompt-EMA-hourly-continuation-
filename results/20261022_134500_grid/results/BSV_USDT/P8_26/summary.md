# EMA Hourly Continuation — BSV/USDT P8_26

**Symbol:** BSV/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1659 |
| net_profit_factor | 0.3354 |
| net_win_rate | 0.4008 |
| gross_profit_factor | 0.8015 |
| gross_win_rate | 0.4340 |
| sharpe_ratio | -13.2421 |
| sortino_ratio | -7.6554 |
| max_drawdown | 0.9999 |
| cagr | -0.9789 |
| net_avg_win | 7.5883 |
| net_avg_loss | -15.1364 |
| avg_hold_time_bars | 3.7366 |
| exposure | 0.2818 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
