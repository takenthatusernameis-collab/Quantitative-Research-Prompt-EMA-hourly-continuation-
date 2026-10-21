# EMA Hourly Continuation — FIL/USDT P34_50

**Symbol:** FIL/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 212 |
| net_profit_factor | 0.8467 |
| net_win_rate | 0.5472 |
| gross_profit_factor | 1.2025 |
| gross_win_rate | 0.5472 |
| sharpe_ratio | -0.7288 |
| sortino_ratio | -0.1539 |
| max_drawdown | 0.1850 |
| cagr | -0.0689 |
| net_avg_win | 78.1038 |
| net_avg_loss | -111.4668 |
| avg_hold_time_bars | 4.8302 |
| exposure | 0.0465 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
