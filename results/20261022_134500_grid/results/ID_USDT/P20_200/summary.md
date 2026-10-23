# EMA Hourly Continuation — ID/USDT P20_200

**Symbol:** ID/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 366 |
| net_profit_factor | 0.7234 |
| net_win_rate | 0.5027 |
| gross_profit_factor | 1.0268 |
| gross_win_rate | 0.5109 |
| sharpe_ratio | -1.7750 |
| sortino_ratio | -0.4803 |
| max_drawdown | 0.4551 |
| cagr | -0.2027 |
| net_avg_win | 61.8830 |
| net_avg_loss | -86.4812 |
| avg_hold_time_bars | 39.6284 |
| exposure | 0.6564 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
