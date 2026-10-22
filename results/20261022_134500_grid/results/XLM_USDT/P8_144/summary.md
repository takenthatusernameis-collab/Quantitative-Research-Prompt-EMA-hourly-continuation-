# EMA Hourly Continuation — XLM/USDT P8_144

**Symbol:** XLM/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 564 |
| net_profit_factor | 0.5226 |
| net_win_rate | 0.4734 |
| gross_profit_factor | 0.9352 |
| gross_win_rate | 0.4840 |
| sharpe_ratio | -4.2465 |
| sortino_ratio | -1.3984 |
| max_drawdown | 0.8380 |
| cagr | -0.5035 |
| net_avg_win | 33.9407 |
| net_avg_loss | -58.3807 |
| avg_hold_time_bars | 28.1649 |
| exposure | 0.7220 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
