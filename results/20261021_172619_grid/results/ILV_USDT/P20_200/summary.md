# EMA Hourly Continuation — ILV/USDT P20_200

**Symbol:** ILV/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 321 |
| net_profit_factor | 0.9610 |
| net_win_rate | 0.5358 |
| gross_profit_factor | 1.1490 |
| gross_win_rate | 0.5358 |
| sharpe_ratio | -0.1760 |
| sortino_ratio | -0.0456 |
| max_drawdown | 0.1534 |
| cagr | -0.0260 |
| net_avg_win | 91.6204 |
| net_avg_loss | -110.0566 |
| avg_hold_time_bars | 43.7508 |
| exposure | 0.6384 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
