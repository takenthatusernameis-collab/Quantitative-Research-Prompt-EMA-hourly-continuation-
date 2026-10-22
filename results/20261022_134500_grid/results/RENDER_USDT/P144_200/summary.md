# EMA Hourly Continuation — RENDER/USDT P144_200

**Symbol:** RENDER/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 320 |
| net_profit_factor | 0.5511 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 1.0027 |
| gross_win_rate | 0.5125 |
| sharpe_ratio | -3.3288 |
| sortino_ratio | -0.9018 |
| max_drawdown | 0.6193 |
| cagr | -0.3574 |
| net_avg_win | 47.2363 |
| net_avg_loss | -85.7182 |
| avg_hold_time_bars | 4.8719 |
| exposure | 0.0823 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
