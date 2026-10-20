# EMA Hourly Continuation — XNO/USDT P89_100

**Symbol:** XNO/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 770 |
| net_profit_factor | 0.2138 |
| net_win_rate | 0.3195 |
| gross_profit_factor | 0.6202 |
| gross_win_rate | 0.3597 |
| sharpe_ratio | -12.3145 |
| sortino_ratio | -5.0391 |
| max_drawdown | 0.9986 |
| cagr | -0.9271 |
| net_avg_win | 11.0414 |
| net_avg_loss | -24.2409 |
| avg_hold_time_bars | 2.4519 |
| exposure | 0.0858 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
