# EMA Hourly Continuation — API3/USDT P20_34

**Symbol:** API3/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1201 |
| net_profit_factor | 0.4883 |
| net_win_rate | 0.4288 |
| gross_profit_factor | 0.9557 |
| gross_win_rate | 0.4463 |
| sharpe_ratio | -9.9542 |
| sortino_ratio | -4.8950 |
| max_drawdown | 0.9978 |
| cagr | -0.9119 |
| net_avg_win | 18.4854 |
| net_avg_loss | -28.4221 |
| avg_hold_time_bars | 2.8393 |
| exposure | 0.1550 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
