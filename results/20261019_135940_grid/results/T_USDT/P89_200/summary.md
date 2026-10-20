# EMA Hourly Continuation — T/USDT P89_200

**Symbol:** T/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 373 |
| net_profit_factor | 0.5789 |
| net_win_rate | 0.4799 |
| gross_profit_factor | 0.9542 |
| gross_win_rate | 0.4960 |
| sharpe_ratio | -3.0839 |
| sortino_ratio | -0.8414 |
| max_drawdown | 0.6422 |
| cagr | -0.3301 |
| net_avg_win | 48.8387 |
| net_avg_loss | -77.8476 |
| avg_hold_time_bars | 13.4263 |
| exposure | 0.2266 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
