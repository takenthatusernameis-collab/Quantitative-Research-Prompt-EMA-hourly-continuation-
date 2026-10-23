# EMA Hourly Continuation — LQTY/USDT P12_50

**Symbol:** LQTY/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 988 |
| net_profit_factor | 0.5166 |
| net_win_rate | 0.4605 |
| gross_profit_factor | 0.8289 |
| gross_win_rate | 0.4706 |
| sharpe_ratio | -6.0324 |
| sortino_ratio | -2.6467 |
| max_drawdown | 0.9628 |
| cagr | -0.7261 |
| net_avg_win | 22.5913 |
| net_avg_loss | -37.3317 |
| avg_hold_time_bars | 9.0577 |
| exposure | 0.4050 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
