# EMA Hourly Continuation — UQC/USDT P89_144

**Symbol:** UQC/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 337 |
| net_profit_factor | 0.1439 |
| net_win_rate | 0.2136 |
| gross_profit_factor | 0.3534 |
| gross_win_rate | 0.2522 |
| sharpe_ratio | -9.7332 |
| sortino_ratio | -2.6702 |
| max_drawdown | 0.9775 |
| cagr | -0.7779 |
| net_avg_win | 22.8227 |
| net_avg_loss | -43.0884 |
| avg_hold_time_bars | 20.0356 |
| exposure | 0.3056 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
