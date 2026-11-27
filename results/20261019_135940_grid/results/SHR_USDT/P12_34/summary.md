# EMA Hourly Continuation — SHR/USDT P12_34

**Symbol:** SHR/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1505 |
| net_profit_factor | 0.3508 |
| net_win_rate | 0.3189 |
| gross_profit_factor | 0.5679 |
| gross_win_rate | 0.3236 |
| sharpe_ratio | -13.7461 |
| sortino_ratio | -7.4635 |
| max_drawdown | 0.9999 |
| cagr | -0.9751 |
| net_avg_win | 11.2581 |
| net_avg_loss | -15.0273 |
| avg_hold_time_bars | 3.9183 |
| exposure | 0.2668 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
