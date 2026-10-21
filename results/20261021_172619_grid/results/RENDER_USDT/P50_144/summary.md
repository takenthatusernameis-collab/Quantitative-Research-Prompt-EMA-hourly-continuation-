# EMA Hourly Continuation — RENDER/USDT P50_144

**Symbol:** RENDER/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 298 |
| net_profit_factor | 0.8259 |
| net_win_rate | 0.5034 |
| gross_profit_factor | 1.0089 |
| gross_win_rate | 0.5034 |
| sharpe_ratio | -1.1234 |
| sortino_ratio | -0.2991 |
| max_drawdown | 0.3359 |
| cagr | -0.1301 |
| net_avg_win | 82.2754 |
| net_avg_loss | -100.9683 |
| avg_hold_time_bars | 16.4295 |
| exposure | 0.2584 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
