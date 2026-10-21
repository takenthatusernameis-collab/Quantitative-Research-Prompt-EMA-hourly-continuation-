# EMA Hourly Continuation — XDC/USDT P8_26

**Symbol:** XDC/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 553 |
| net_profit_factor | 0.5458 |
| net_win_rate | 0.4720 |
| gross_profit_factor | 0.8785 |
| gross_win_rate | 0.4720 |
| sharpe_ratio | -4.2869 |
| sortino_ratio | -1.4475 |
| max_drawdown | 0.8149 |
| cagr | -0.4838 |
| net_avg_win | 37.2902 |
| net_avg_loss | -61.0694 |
| avg_hold_time_bars | 7.1646 |
| exposure | 0.1801 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
