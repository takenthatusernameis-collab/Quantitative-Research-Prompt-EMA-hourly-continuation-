# EMA Hourly Continuation — BONK/USDT P34_50

**Symbol:** BONK/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 193 |
| net_profit_factor | 0.9616 |
| net_win_rate | 0.5596 |
| gross_profit_factor | 1.2595 |
| gross_win_rate | 0.5596 |
| sharpe_ratio | -0.1443 |
| sortino_ratio | -0.0292 |
| max_drawdown | 0.2429 |
| cagr | -0.0164 |
| net_avg_win | 94.5628 |
| net_avg_loss | -124.9444 |
| avg_hold_time_bars | 5.0674 |
| exposure | 0.0445 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
