# EMA Hourly Continuation — ID/USDT P8_21

**Symbol:** ID/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 781 |
| net_profit_factor | 0.6786 |
| net_win_rate | 0.4891 |
| gross_profit_factor | 0.9929 |
| gross_win_rate | 0.4891 |
| sharpe_ratio | -3.7642 |
| sortino_ratio | -1.5052 |
| max_drawdown | 0.8377 |
| cagr | -0.4974 |
| net_avg_win | 45.5137 |
| net_avg_loss | -64.2168 |
| avg_hold_time_bars | 5.8681 |
| exposure | 0.2074 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
