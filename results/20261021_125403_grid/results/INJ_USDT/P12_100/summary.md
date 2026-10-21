# EMA Hourly Continuation — INJ/USDT P12_100

**Symbol:** INJ/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 478 |
| net_profit_factor | 0.7899 |
| net_win_rate | 0.4812 |
| gross_profit_factor | 0.9334 |
| gross_win_rate | 0.4812 |
| sharpe_ratio | -1.6850 |
| sortino_ratio | -0.5249 |
| max_drawdown | 0.4621 |
| cagr | -0.2158 |
| net_avg_win | 74.6984 |
| net_avg_loss | -87.7022 |
| avg_hold_time_bars | 25.7992 |
| exposure | 0.5605 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
