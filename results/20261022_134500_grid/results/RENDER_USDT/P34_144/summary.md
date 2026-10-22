# EMA Hourly Continuation — RENDER/USDT P34_144

**Symbol:** RENDER/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 416 |
| net_profit_factor | 0.7034 |
| net_win_rate | 0.4880 |
| gross_profit_factor | 0.9631 |
| gross_win_rate | 0.4880 |
| sharpe_ratio | -2.5035 |
| sortino_ratio | -0.7734 |
| max_drawdown | 0.5781 |
| cagr | -0.3079 |
| net_avg_win | 64.1156 |
| net_avg_loss | -86.8735 |
| avg_hold_time_bars | 18.3534 |
| exposure | 0.4030 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
