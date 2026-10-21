# EMA Hourly Continuation — LINK/USDT P20_55

**Symbol:** LINK/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 470 |
| net_profit_factor | 0.6523 |
| net_win_rate | 0.4532 |
| gross_profit_factor | 0.8734 |
| gross_win_rate | 0.4532 |
| sharpe_ratio | -3.3205 |
| sortino_ratio | -1.0251 |
| max_drawdown | 0.7057 |
| cagr | -0.3757 |
| net_avg_win | 61.0959 |
| net_avg_loss | -77.6292 |
| avg_hold_time_bars | 9.4851 |
| exposure | 0.2026 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
