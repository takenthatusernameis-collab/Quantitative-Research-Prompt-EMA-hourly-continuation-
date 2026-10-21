# EMA Hourly Continuation — FLOKI/USDT P50_144

**Symbol:** FLOKI/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 346 |
| net_profit_factor | 0.8324 |
| net_win_rate | 0.5058 |
| gross_profit_factor | 1.0178 |
| gross_win_rate | 0.5058 |
| sharpe_ratio | -1.0350 |
| sortino_ratio | -0.2762 |
| max_drawdown | 0.3074 |
| cagr | -0.1206 |
| net_avg_win | 78.3164 |
| net_avg_loss | -96.2808 |
| avg_hold_time_bars | 19.1734 |
| exposure | 0.3015 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
