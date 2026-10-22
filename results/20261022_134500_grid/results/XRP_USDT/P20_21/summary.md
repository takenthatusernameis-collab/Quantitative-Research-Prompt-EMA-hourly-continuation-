# EMA Hourly Continuation — XRP/USDT P20_21

**Symbol:** XRP/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1206 |
| net_profit_factor | 0.0748 |
| net_win_rate | 0.2504 |
| gross_profit_factor | 0.5941 |
| gross_win_rate | 0.3483 |
| sharpe_ratio | -20.9632 |
| sortino_ratio | -12.1585 |
| max_drawdown | 1.0000 |
| cagr | -0.9991 |
| net_avg_win | 2.6766 |
| net_avg_loss | -11.9561 |
| avg_hold_time_bars | 1.5439 |
| exposure | 0.0846 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
