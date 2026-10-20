# EMA Hourly Continuation — DBR/USDT P34_100

**Symbol:** DBR/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 445 |
| net_profit_factor | 0.4651 |
| net_win_rate | 0.4292 |
| gross_profit_factor | 0.8006 |
| gross_win_rate | 0.4472 |
| sharpe_ratio | -5.5931 |
| sortino_ratio | -1.8533 |
| max_drawdown | 0.8455 |
| cagr | -0.5953 |
| net_avg_win | 38.1229 |
| net_avg_loss | -61.6315 |
| avg_hold_time_bars | 10.4449 |
| exposure | 0.2643 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
