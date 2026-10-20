# EMA Hourly Continuation — POKT/USDT P12_200

**Symbol:** POKT/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 542 |
| net_profit_factor | 0.6058 |
| net_win_rate | 0.4262 |
| gross_profit_factor | 0.8332 |
| gross_win_rate | 0.4354 |
| sharpe_ratio | -4.2068 |
| sortino_ratio | -1.3715 |
| max_drawdown | 0.8124 |
| cagr | -0.4752 |
| net_avg_win | 53.4362 |
| net_avg_loss | -65.5210 |
| avg_hold_time_bars | 28.9815 |
| exposure | 0.7108 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
