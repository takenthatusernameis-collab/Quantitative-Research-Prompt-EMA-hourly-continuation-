# EMA Hourly Continuation — BLZ/USDT P34_200

**Symbol:** BLZ/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 452 |
| net_profit_factor | 0.6420 |
| net_win_rate | 0.4535 |
| gross_profit_factor | 0.9003 |
| gross_win_rate | 0.4580 |
| sharpe_ratio | -3.4223 |
| sortino_ratio | -1.0260 |
| max_drawdown | 0.7220 |
| cagr | -0.3810 |
| net_avg_win | 61.3842 |
| net_avg_loss | -79.3592 |
| avg_hold_time_bars | 26.1128 |
| exposure | 0.5341 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
