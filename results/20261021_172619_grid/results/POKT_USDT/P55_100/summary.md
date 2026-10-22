# EMA Hourly Continuation — POKT/USDT P55_100

**Symbol:** POKT/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 380 |
| net_profit_factor | 0.7017 |
| net_win_rate | 0.4684 |
| gross_profit_factor | 0.9311 |
| gross_win_rate | 0.4684 |
| sharpe_ratio | -2.4905 |
| sortino_ratio | -0.6894 |
| max_drawdown | 0.5778 |
| cagr | -0.2718 |
| net_avg_win | 72.7672 |
| net_avg_loss | -91.3838 |
| avg_hold_time_bars | 9.4684 |
| exposure | 0.1628 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
