# EMA Hourly Continuation — KCS/USDT P8_50

**Symbol:** KCS/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 597 |
| net_profit_factor | 0.4678 |
| net_win_rate | 0.4389 |
| gross_profit_factor | 0.7831 |
| gross_win_rate | 0.4422 |
| sharpe_ratio | -5.5892 |
| sortino_ratio | -1.9571 |
| max_drawdown | 0.9004 |
| cagr | -0.5994 |
| net_avg_win | 30.1727 |
| net_avg_loss | -50.4479 |
| avg_hold_time_bars | 16.7102 |
| exposure | 0.4535 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
