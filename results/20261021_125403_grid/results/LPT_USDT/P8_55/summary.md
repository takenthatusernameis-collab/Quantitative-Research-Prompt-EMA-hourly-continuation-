# EMA Hourly Continuation — LPT/USDT P8_55

**Symbol:** LPT/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 724 |
| net_profit_factor | 0.7833 |
| net_win_rate | 0.4876 |
| gross_profit_factor | 0.9818 |
| gross_win_rate | 0.4876 |
| sharpe_ratio | -2.5112 |
| sortino_ratio | -0.9641 |
| max_drawdown | 0.7026 |
| cagr | -0.3597 |
| net_avg_win | 68.9594 |
| net_avg_loss | -83.7695 |
| avg_hold_time_bars | 13.9475 |
| exposure | 0.4590 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
