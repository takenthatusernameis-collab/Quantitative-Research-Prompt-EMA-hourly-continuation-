# EMA Hourly Continuation — CFX/USDT P12_200

**Symbol:** CFX/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 356 |
| net_profit_factor | 0.6801 |
| net_win_rate | 0.4916 |
| gross_profit_factor | 0.9651 |
| gross_win_rate | 0.4916 |
| sharpe_ratio | -2.2921 |
| sortino_ratio | -0.6011 |
| max_drawdown | 0.5472 |
| cagr | -0.2544 |
| net_avg_win | 63.3640 |
| net_avg_loss | -90.0804 |
| avg_hold_time_bars | 46.7837 |
| exposure | 0.7570 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
