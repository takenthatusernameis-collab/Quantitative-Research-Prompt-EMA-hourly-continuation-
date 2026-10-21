# EMA Hourly Continuation — ZRO/USDT P20_55

**Symbol:** ZRO/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 505 |
| net_profit_factor | 0.8556 |
| net_win_rate | 0.5149 |
| gross_profit_factor | 1.0577 |
| gross_win_rate | 0.5149 |
| sharpe_ratio | -1.1191 |
| sortino_ratio | -0.3753 |
| max_drawdown | 0.3587 |
| cagr | -0.1611 |
| net_avg_win | 76.6217 |
| net_avg_loss | -95.0352 |
| avg_hold_time_bars | 8.3644 |
| exposure | 0.2067 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
