# EMA Hourly Continuation — POPCAT/USDT P12_200

**Symbol:** POPCAT/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 279 |
| net_profit_factor | 0.8402 |
| net_win_rate | 0.4875 |
| gross_profit_factor | 0.9524 |
| gross_win_rate | 0.4875 |
| sharpe_ratio | -0.9853 |
| sortino_ratio | -0.2530 |
| max_drawdown | 0.2889 |
| cagr | -0.1120 |
| net_avg_win | 87.5341 |
| net_avg_loss | -99.0844 |
| avg_hold_time_bars | 48.5986 |
| exposure | 0.7163 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
