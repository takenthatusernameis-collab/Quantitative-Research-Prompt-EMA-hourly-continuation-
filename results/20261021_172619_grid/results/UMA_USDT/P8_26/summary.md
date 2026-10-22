# EMA Hourly Continuation — UMA/USDT P8_26

**Symbol:** UMA/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 798 |
| net_profit_factor | 0.6479 |
| net_win_rate | 0.4812 |
| gross_profit_factor | 0.9098 |
| gross_win_rate | 0.4812 |
| sharpe_ratio | -4.0108 |
| sortino_ratio | -1.6198 |
| max_drawdown | 0.8497 |
| cagr | -0.5249 |
| net_avg_win | 40.5286 |
| net_avg_loss | -58.0201 |
| avg_hold_time_bars | 6.3972 |
| exposure | 0.2320 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
