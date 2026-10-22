# EMA Hourly Continuation — SOL/USDT P55_89

**Symbol:** SOL/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 624 |
| net_profit_factor | 0.3865 |
| net_win_rate | 0.4455 |
| gross_profit_factor | 0.8626 |
| gross_win_rate | 0.4744 |
| sharpe_ratio | -6.9854 |
| sortino_ratio | -2.4641 |
| max_drawdown | 0.9584 |
| cagr | -0.7161 |
| net_avg_win | 21.6993 |
| net_avg_loss | -45.1124 |
| avg_hold_time_bars | 3.9263 |
| exposure | 0.1114 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
