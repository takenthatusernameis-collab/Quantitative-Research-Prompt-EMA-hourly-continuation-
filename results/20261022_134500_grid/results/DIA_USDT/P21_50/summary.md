# EMA Hourly Continuation — DIA/USDT P21_50

**Symbol:** DIA/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 955 |
| net_profit_factor | 0.4376 |
| net_win_rate | 0.4346 |
| gross_profit_factor | 0.7865 |
| gross_win_rate | 0.4503 |
| sharpe_ratio | -7.5395 |
| sortino_ratio | -3.2582 |
| max_drawdown | 0.9830 |
| cagr | -0.7996 |
| net_avg_win | 18.4208 |
| net_avg_loss | -32.3543 |
| avg_hold_time_bars | 5.0901 |
| exposure | 0.2200 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
