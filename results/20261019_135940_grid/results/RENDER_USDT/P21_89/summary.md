# EMA Hourly Continuation — RENDER/USDT P21_89

**Symbol:** RENDER/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 649 |
| net_profit_factor | 0.6495 |
| net_win_rate | 0.4854 |
| gross_profit_factor | 0.9511 |
| gross_win_rate | 0.4900 |
| sharpe_ratio | -3.8077 |
| sortino_ratio | -1.4720 |
| max_drawdown | 0.7965 |
| cagr | -0.5037 |
| net_avg_win | 45.8975 |
| net_avg_loss | -66.6463 |
| avg_hold_time_bars | 9.8274 |
| exposure | 0.3366 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
