# EMA Hourly Continuation — MANTA/USDT P20_50

**Symbol:** MANTA/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 512 |
| net_profit_factor | 0.6818 |
| net_win_rate | 0.4629 |
| gross_profit_factor | 0.8798 |
| gross_win_rate | 0.4629 |
| sharpe_ratio | -2.9604 |
| sortino_ratio | -0.9539 |
| max_drawdown | 0.6729 |
| cagr | -0.3546 |
| net_avg_win | 60.3033 |
| net_avg_loss | -76.2248 |
| avg_hold_time_bars | 8.9004 |
| exposure | 0.2071 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
