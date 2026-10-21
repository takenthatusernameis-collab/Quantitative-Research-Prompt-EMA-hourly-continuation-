# EMA Hourly Continuation — SUI/USDT P144_200

**Symbol:** SUI/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 192 |
| net_profit_factor | 0.6670 |
| net_win_rate | 0.4740 |
| gross_profit_factor | 0.8923 |
| gross_win_rate | 0.4740 |
| sharpe_ratio | -1.7304 |
| sortino_ratio | -0.3426 |
| max_drawdown | 0.3459 |
| cagr | -0.1451 |
| net_avg_win | 71.6377 |
| net_avg_loss | -96.7649 |
| avg_hold_time_bars | 6.4271 |
| exposure | 0.0561 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
