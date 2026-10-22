# EMA Hourly Continuation — ELON/USDT P8_34

**Symbol:** ELON/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 716 |
| net_profit_factor | 0.6815 |
| net_win_rate | 0.4749 |
| gross_profit_factor | 0.9011 |
| gross_win_rate | 0.4749 |
| sharpe_ratio | -3.3725 |
| sortino_ratio | -1.2887 |
| max_drawdown | 0.7748 |
| cagr | -0.4460 |
| net_avg_win | 48.6601 |
| net_avg_loss | -64.5626 |
| avg_hold_time_bars | 8.2095 |
| exposure | 0.2672 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
