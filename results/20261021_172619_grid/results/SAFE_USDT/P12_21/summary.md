# EMA Hourly Continuation — SAFE/USDT P12_21

**Symbol:** SAFE/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 373 |
| net_profit_factor | 0.6847 |
| net_win_rate | 0.4933 |
| gross_profit_factor | 0.9653 |
| gross_win_rate | 0.4933 |
| sharpe_ratio | -2.2742 |
| sortino_ratio | -0.6324 |
| max_drawdown | 0.5176 |
| cagr | -0.2504 |
| net_avg_win | 60.4747 |
| net_avg_loss | -85.9869 |
| avg_hold_time_bars | 7.2466 |
| exposure | 0.1238 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
