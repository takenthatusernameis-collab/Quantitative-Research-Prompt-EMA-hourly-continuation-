# EMA Hourly Continuation — MERL/USDT P26_144

**Symbol:** MERL/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 484 |
| net_profit_factor | 0.6544 |
| net_win_rate | 0.4401 |
| gross_profit_factor | 0.8557 |
| gross_win_rate | 0.4421 |
| sharpe_ratio | -3.4645 |
| sortino_ratio | -1.0718 |
| max_drawdown | 0.7444 |
| cagr | -0.3976 |
| net_avg_win | 63.8964 |
| net_avg_loss | -76.7495 |
| avg_hold_time_bars | 21.8202 |
| exposure | 0.4814 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
