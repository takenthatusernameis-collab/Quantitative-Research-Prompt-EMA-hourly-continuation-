# EMA Hourly Continuation — CFG/USDT P20_34

**Symbol:** CFG/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 237 |
| net_profit_factor | 0.4412 |
| net_win_rate | 0.3924 |
| gross_profit_factor | 0.6017 |
| gross_win_rate | 0.3924 |
| sharpe_ratio | -3.4561 |
| sortino_ratio | -0.7526 |
| max_drawdown | 0.5866 |
| cagr | -0.2943 |
| net_avg_win | 49.5139 |
| net_avg_loss | -72.4818 |
| avg_hold_time_bars | 29.0675 |
| exposure | 0.3131 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
