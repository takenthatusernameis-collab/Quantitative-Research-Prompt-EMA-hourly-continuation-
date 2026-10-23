# EMA Hourly Continuation — PIXEL/USDT P34_200

**Symbol:** PIXEL/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 377 |
| net_profit_factor | 0.8764 |
| net_win_rate | 0.5252 |
| gross_profit_factor | 1.1138 |
| gross_win_rate | 0.5305 |
| sharpe_ratio | -0.7530 |
| sortino_ratio | -0.2094 |
| max_drawdown | 0.2546 |
| cagr | -0.0956 |
| net_avg_win | 80.1731 |
| net_avg_loss | -101.1874 |
| avg_hold_time_bars | 30.7772 |
| exposure | 0.5250 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
