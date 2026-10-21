# EMA Hourly Continuation — VELO/USDT P34_200

**Symbol:** VELO/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 318 |
| net_profit_factor | 0.9756 |
| net_win_rate | 0.5314 |
| gross_profit_factor | 1.1156 |
| gross_win_rate | 0.5314 |
| sharpe_ratio | -0.0781 |
| sortino_ratio | -0.0201 |
| max_drawdown | 0.1895 |
| cagr | -0.0150 |
| net_avg_win | 87.9908 |
| net_avg_loss | -102.3003 |
| avg_hold_time_bars | 33.3113 |
| exposure | 0.4815 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
