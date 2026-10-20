# EMA Hourly Continuation — ORBS/USDT P20_144

**Symbol:** ORBS/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 527 |
| net_profit_factor | 0.5998 |
| net_win_rate | 0.4440 |
| gross_profit_factor | 0.9137 |
| gross_win_rate | 0.4478 |
| sharpe_ratio | -4.5938 |
| sortino_ratio | -1.4756 |
| max_drawdown | 0.8425 |
| cagr | -0.5125 |
| net_avg_win | 53.5065 |
| net_avg_loss | -71.2450 |
| avg_hold_time_bars | 24.7837 |
| exposure | 0.5937 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
