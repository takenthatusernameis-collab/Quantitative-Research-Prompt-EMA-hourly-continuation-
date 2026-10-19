# EMA Hourly Continuation — CRV/USDT P12_50

**Symbol:** CRV/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1068 |
| net_profit_factor | 0.5798 |
| net_win_rate | 0.4757 |
| gross_profit_factor | 0.9426 |
| gross_win_rate | 0.4897 |
| sharpe_ratio | -5.6780 |
| sortino_ratio | -2.6069 |
| max_drawdown | 0.9589 |
| cagr | -0.7156 |
| net_avg_win | 26.0054 |
| net_avg_loss | -40.6887 |
| avg_hold_time_bars | 6.9410 |
| exposure | 0.3370 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
