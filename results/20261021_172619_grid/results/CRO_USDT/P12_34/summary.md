# EMA Hourly Continuation — CRO/USDT P12_34

**Symbol:** CRO/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 594 |
| net_profit_factor | 0.5267 |
| net_win_rate | 0.4545 |
| gross_profit_factor | 0.8098 |
| gross_win_rate | 0.4562 |
| sharpe_ratio | -4.6521 |
| sortino_ratio | -1.6211 |
| max_drawdown | 0.8502 |
| cagr | -0.5274 |
| net_avg_win | 34.9438 |
| net_avg_loss | -55.2859 |
| avg_hold_time_bars | 7.0842 |
| exposure | 0.1913 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
