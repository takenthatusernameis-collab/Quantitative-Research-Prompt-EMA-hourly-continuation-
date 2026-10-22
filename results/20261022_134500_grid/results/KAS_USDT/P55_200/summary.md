# EMA Hourly Continuation — KAS/USDT P55_200

**Symbol:** KAS/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 447 |
| net_profit_factor | 0.4823 |
| net_win_rate | 0.4497 |
| gross_profit_factor | 0.7915 |
| gross_win_rate | 0.4586 |
| sharpe_ratio | -4.3596 |
| sortino_ratio | -1.2856 |
| max_drawdown | 0.8076 |
| cagr | -0.4702 |
| net_avg_win | 36.9497 |
| net_avg_loss | -62.5962 |
| avg_hold_time_bars | 14.8725 |
| exposure | 0.3022 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
