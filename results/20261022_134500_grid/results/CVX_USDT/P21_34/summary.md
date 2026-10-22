# EMA Hourly Continuation — CVX/USDT P21_34

**Symbol:** CVX/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1116 |
| net_profit_factor | 0.3860 |
| net_win_rate | 0.4194 |
| gross_profit_factor | 0.7914 |
| gross_win_rate | 0.4346 |
| sharpe_ratio | -9.9579 |
| sortino_ratio | -4.7256 |
| max_drawdown | 0.9973 |
| cagr | -0.9051 |
| net_avg_win | 13.3946 |
| net_avg_loss | -25.0643 |
| avg_hold_time_bars | 2.7168 |
| exposure | 0.1378 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
