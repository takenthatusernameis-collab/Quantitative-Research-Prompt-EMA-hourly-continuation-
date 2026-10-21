# EMA Hourly Continuation — COTI/USDT P34_144

**Symbol:** COTI/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 354 |
| net_profit_factor | 0.9333 |
| net_win_rate | 0.5311 |
| gross_profit_factor | 1.1207 |
| gross_win_rate | 0.5311 |
| sharpe_ratio | -0.3457 |
| sortino_ratio | -0.0939 |
| max_drawdown | 0.2395 |
| cagr | -0.0469 |
| net_avg_win | 84.5973 |
| net_avg_loss | -102.6596 |
| avg_hold_time_bars | 25.5028 |
| exposure | 0.4104 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
