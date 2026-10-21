# EMA Hourly Continuation — ZRO/USDT P89_200

**Symbol:** ZRO/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 251 |
| net_profit_factor | 0.8673 |
| net_win_rate | 0.5139 |
| gross_profit_factor | 1.0399 |
| gross_win_rate | 0.5139 |
| sharpe_ratio | -0.6513 |
| sortino_ratio | -0.1539 |
| max_drawdown | 0.2732 |
| cagr | -0.0704 |
| net_avg_win | 79.2841 |
| net_avg_loss | -96.6608 |
| avg_hold_time_bars | 11.2311 |
| exposure | 0.1380 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
