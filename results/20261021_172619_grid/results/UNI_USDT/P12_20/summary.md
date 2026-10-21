# EMA Hourly Continuation — UNI/USDT P12_20

**Symbol:** UNI/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 221 |
| net_profit_factor | 0.6845 |
| net_win_rate | 0.4887 |
| gross_profit_factor | 0.9621 |
| gross_win_rate | 0.4887 |
| sharpe_ratio | -1.7715 |
| sortino_ratio | -0.3778 |
| max_drawdown | 0.3911 |
| cagr | -0.1584 |
| net_avg_win | 70.6118 |
| net_avg_loss | -98.5898 |
| avg_hold_time_bars | 4.3122 |
| exposure | 0.0433 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
