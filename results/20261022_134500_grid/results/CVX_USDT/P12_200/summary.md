# EMA Hourly Continuation — CVX/USDT P12_200

**Symbol:** CVX/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 339 |
| net_profit_factor | 0.7756 |
| net_win_rate | 0.5015 |
| gross_profit_factor | 0.9946 |
| gross_win_rate | 0.5044 |
| sharpe_ratio | -1.3834 |
| sortino_ratio | -0.3595 |
| max_drawdown | 0.3962 |
| cagr | -0.1572 |
| net_avg_win | 70.9899 |
| net_avg_loss | -92.0688 |
| avg_hold_time_bars | 49.4248 |
| exposure | 0.7616 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
