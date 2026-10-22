# EMA Hourly Continuation — XTZ/USDT P20_34

**Symbol:** XTZ/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1222 |
| net_profit_factor | 0.2918 |
| net_win_rate | 0.3985 |
| gross_profit_factor | 0.8210 |
| gross_win_rate | 0.4476 |
| sharpe_ratio | -12.2946 |
| sortino_ratio | -6.1508 |
| max_drawdown | 0.9996 |
| cagr | -0.9574 |
| net_avg_win | 8.4557 |
| net_avg_loss | -19.2031 |
| avg_hold_time_bars | 2.8584 |
| exposure | 0.1588 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
