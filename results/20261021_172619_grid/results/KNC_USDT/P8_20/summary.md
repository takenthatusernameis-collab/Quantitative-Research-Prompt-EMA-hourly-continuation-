# EMA Hourly Continuation — KNC/USDT P8_20

**Symbol:** KNC/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 787 |
| net_profit_factor | 0.5744 |
| net_win_rate | 0.4638 |
| gross_profit_factor | 0.9231 |
| gross_win_rate | 0.4638 |
| sharpe_ratio | -5.6306 |
| sortino_ratio | -2.2616 |
| max_drawdown | 0.9306 |
| cagr | -0.6493 |
| net_avg_win | 34.3135 |
| net_avg_loss | -51.6695 |
| avg_hold_time_bars | 5.9543 |
| exposure | 0.2130 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
