# EMA Hourly Continuation — AGLD/USDT P12_20

**Symbol:** AGLD/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 574 |
| net_profit_factor | 0.6096 |
| net_win_rate | 0.4721 |
| gross_profit_factor | 0.9012 |
| gross_win_rate | 0.4721 |
| sharpe_ratio | -3.7646 |
| sortino_ratio | -1.2889 |
| max_drawdown | 0.7865 |
| cagr | -0.4462 |
| net_avg_win | 44.6402 |
| net_avg_loss | -65.4938 |
| avg_hold_time_bars | 5.0418 |
| exposure | 0.1310 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
