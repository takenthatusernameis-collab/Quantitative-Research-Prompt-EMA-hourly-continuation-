# EMA Hourly Continuation — SAFE/USDT P50_100

**Symbol:** SAFE/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 592 |
| net_profit_factor | 0.5910 |
| net_win_rate | 0.4797 |
| gross_profit_factor | 0.9566 |
| gross_win_rate | 0.4865 |
| sharpe_ratio | -3.9534 |
| sortino_ratio | -1.3666 |
| max_drawdown | 0.8132 |
| cagr | -0.4761 |
| net_avg_win | 40.7179 |
| net_avg_loss | -63.5328 |
| avg_hold_time_bars | 7.3497 |
| exposure | 0.1993 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
