# EMA Hourly Continuation — VET/USDT P20_200

**Symbol:** VET/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 430 |
| net_profit_factor | 0.6658 |
| net_win_rate | 0.4837 |
| gross_profit_factor | 0.9802 |
| gross_win_rate | 0.4977 |
| sharpe_ratio | -2.7040 |
| sortino_ratio | -0.7883 |
| max_drawdown | 0.6417 |
| cagr | -0.3124 |
| net_avg_win | 58.3942 |
| net_avg_loss | -82.1683 |
| avg_hold_time_bars | 31.5651 |
| exposure | 0.6170 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
