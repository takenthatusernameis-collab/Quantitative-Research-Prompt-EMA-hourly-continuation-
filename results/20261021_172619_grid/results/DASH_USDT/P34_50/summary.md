# EMA Hourly Continuation — DASH/USDT P34_50

**Symbol:** DASH/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 225 |
| net_profit_factor | 0.7885 |
| net_win_rate | 0.5333 |
| gross_profit_factor | 1.1378 |
| gross_win_rate | 0.5333 |
| sharpe_ratio | -1.0748 |
| sortino_ratio | -0.2332 |
| max_drawdown | 0.2482 |
| cagr | -0.1014 |
| net_avg_win | 73.1523 |
| net_avg_loss | -106.0220 |
| avg_hold_time_bars | 5.8933 |
| exposure | 0.0603 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
