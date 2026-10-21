# EMA Hourly Continuation — XTZ/USDT P20_50

**Symbol:** XTZ/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 572 |
| net_profit_factor | 0.6116 |
| net_win_rate | 0.4720 |
| gross_profit_factor | 0.8880 |
| gross_win_rate | 0.4720 |
| sharpe_ratio | -3.5924 |
| sortino_ratio | -1.2302 |
| max_drawdown | 0.7655 |
| cagr | -0.4295 |
| net_avg_win | 44.0737 |
| net_avg_loss | -64.4268 |
| avg_hold_time_bars | 7.4598 |
| exposure | 0.1940 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
