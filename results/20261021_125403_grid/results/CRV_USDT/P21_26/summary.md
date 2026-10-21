# EMA Hourly Continuation — CRV/USDT P21_26

**Symbol:** CRV/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 142 |
| net_profit_factor | 0.6586 |
| net_win_rate | 0.4789 |
| gross_profit_factor | 0.9062 |
| gross_win_rate | 0.4789 |
| sharpe_ratio | -1.4846 |
| sortino_ratio | -0.2531 |
| max_drawdown | 0.2819 |
| cagr | -0.1088 |
| net_avg_win | 71.2805 |
| net_avg_loss | -99.4523 |
| avg_hold_time_bars | 4.4718 |
| exposure | 0.0289 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
