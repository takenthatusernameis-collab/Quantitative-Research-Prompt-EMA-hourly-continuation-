# EMA Hourly Continuation — EDU/USDT P12_200

**Symbol:** EDU/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 376 |
| net_profit_factor | 0.7851 |
| net_win_rate | 0.4787 |
| gross_profit_factor | 0.9139 |
| gross_win_rate | 0.4787 |
| sharpe_ratio | -1.4532 |
| sortino_ratio | -0.4000 |
| max_drawdown | 0.4060 |
| cagr | -0.1701 |
| net_avg_win | 76.1795 |
| net_avg_loss | -89.1056 |
| avg_hold_time_bars | 41.7101 |
| exposure | 0.7097 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
