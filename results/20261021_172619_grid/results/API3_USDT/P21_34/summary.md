# EMA Hourly Continuation — API3/USDT P21_34

**Symbol:** API3/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 363 |
| net_profit_factor | 0.5956 |
| net_win_rate | 0.4518 |
| gross_profit_factor | 0.8497 |
| gross_win_rate | 0.4518 |
| sharpe_ratio | -3.3734 |
| sortino_ratio | -0.9187 |
| max_drawdown | 0.6634 |
| cagr | -0.3454 |
| net_avg_win | 58.8073 |
| net_avg_loss | -81.3766 |
| avg_hold_time_bars | 4.9780 |
| exposure | 0.0821 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
