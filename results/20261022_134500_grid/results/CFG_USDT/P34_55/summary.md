# EMA Hourly Continuation — CFG/USDT P34_55

**Symbol:** CFG/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 931 |
| net_profit_factor | 0.4457 |
| net_win_rate | 0.4447 |
| gross_profit_factor | 0.8709 |
| gross_win_rate | 0.4608 |
| sharpe_ratio | -7.0981 |
| sortino_ratio | -3.0674 |
| max_drawdown | 0.9763 |
| cagr | -0.7726 |
| net_avg_win | 18.9550 |
| net_avg_loss | -34.0522 |
| avg_hold_time_bars | 3.1182 |
| exposure | 0.1320 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
