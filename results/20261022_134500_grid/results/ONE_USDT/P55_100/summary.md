# EMA Hourly Continuation — ONE/USDT P55_100

**Symbol:** ONE/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 624 |
| net_profit_factor | 0.6091 |
| net_win_rate | 0.4647 |
| gross_profit_factor | 0.9864 |
| gross_win_rate | 0.4744 |
| sharpe_ratio | -4.7684 |
| sortino_ratio | -1.6828 |
| max_drawdown | 0.8747 |
| cagr | -0.5552 |
| net_avg_win | 46.7064 |
| net_avg_loss | -66.5790 |
| avg_hold_time_bars | 5.1506 |
| exposure | 0.1461 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
