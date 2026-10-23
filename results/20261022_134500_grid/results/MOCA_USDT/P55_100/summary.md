# EMA Hourly Continuation — MOCA/USDT P55_100

**Symbol:** MOCA/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 556 |
| net_profit_factor | 0.4882 |
| net_win_rate | 0.4353 |
| gross_profit_factor | 0.8157 |
| gross_win_rate | 0.4496 |
| sharpe_ratio | -6.0564 |
| sortino_ratio | -2.1062 |
| max_drawdown | 0.9126 |
| cagr | -0.6495 |
| net_avg_win | 35.7935 |
| net_avg_loss | -56.5062 |
| avg_hold_time_bars | 5.3543 |
| exposure | 0.1492 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
