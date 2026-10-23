# EMA Hourly Continuation — AGLD/USDT P21_200

**Symbol:** AGLD/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 450 |
| net_profit_factor | 0.6846 |
| net_win_rate | 0.4667 |
| gross_profit_factor | 0.9335 |
| gross_win_rate | 0.4756 |
| sharpe_ratio | -2.7610 |
| sortino_ratio | -0.8214 |
| max_drawdown | 0.6598 |
| cagr | -0.3208 |
| net_avg_win | 64.4158 |
| net_avg_loss | -82.3258 |
| avg_hold_time_bars | 29.2467 |
| exposure | 0.5956 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
