# EMA Hourly Continuation — SUPER/USDT P20_21

**Symbol:** SUPER/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1218 |
| net_profit_factor | 0.1865 |
| net_win_rate | 0.3128 |
| gross_profit_factor | 0.7108 |
| gross_win_rate | 0.3998 |
| sharpe_ratio | -16.7598 |
| sortino_ratio | -8.7242 |
| max_drawdown | 1.0000 |
| cagr | -0.9925 |
| net_avg_win | 6.0163 |
| net_avg_loss | -14.6860 |
| avg_hold_time_bars | 1.7775 |
| exposure | 0.0984 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
