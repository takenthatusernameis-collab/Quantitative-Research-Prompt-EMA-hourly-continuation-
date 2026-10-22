# EMA Hourly Continuation — MOCA/USDT P12_21

**Symbol:** MOCA/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 348 |
| net_profit_factor | 0.5166 |
| net_win_rate | 0.4368 |
| gross_profit_factor | 0.7531 |
| gross_win_rate | 0.4368 |
| sharpe_ratio | -3.9145 |
| sortino_ratio | -1.0943 |
| max_drawdown | 0.6880 |
| cagr | -0.3961 |
| net_avg_win | 48.0091 |
| net_avg_loss | -72.0744 |
| avg_hold_time_bars | 5.0948 |
| exposure | 0.0889 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
