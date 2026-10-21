# EMA Hourly Continuation — GALA/USDT P20_34

**Symbol:** GALA/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 327 |
| net_profit_factor | 0.6601 |
| net_win_rate | 0.4648 |
| gross_profit_factor | 0.9038 |
| gross_win_rate | 0.4648 |
| sharpe_ratio | -2.5961 |
| sortino_ratio | -0.6707 |
| max_drawdown | 0.5498 |
| cagr | -0.2645 |
| net_avg_win | 68.6876 |
| net_avg_loss | -90.3822 |
| avg_hold_time_bars | 4.8349 |
| exposure | 0.0719 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
