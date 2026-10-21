# EMA Hourly Continuation — PEOPLE/USDT P8_12

**Symbol:** PEOPLE/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 340 |
| net_profit_factor | 0.6435 |
| net_win_rate | 0.4647 |
| gross_profit_factor | 0.8964 |
| gross_win_rate | 0.4647 |
| sharpe_ratio | -2.7717 |
| sortino_ratio | -0.7280 |
| max_drawdown | 0.5715 |
| cagr | -0.2843 |
| net_avg_win | 65.1008 |
| net_avg_loss | -87.8282 |
| avg_hold_time_bars | 4.9853 |
| exposure | 0.0767 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
