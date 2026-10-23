# EMA Hourly Continuation — IOTX/USDT P144_200

**Symbol:** IOTX/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 451 |
| net_profit_factor | 0.5196 |
| net_win_rate | 0.4834 |
| gross_profit_factor | 0.9500 |
| gross_win_rate | 0.4989 |
| sharpe_ratio | -3.9836 |
| sortino_ratio | -1.1931 |
| max_drawdown | 0.7857 |
| cagr | -0.4384 |
| net_avg_win | 37.9602 |
| net_avg_loss | -68.3556 |
| avg_hold_time_bars | 4.8448 |
| exposure | 0.0993 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
