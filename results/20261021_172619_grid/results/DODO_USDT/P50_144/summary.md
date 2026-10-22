# EMA Hourly Continuation — DODO/USDT P50_144

**Symbol:** DODO/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 387 |
| net_profit_factor | 0.6770 |
| net_win_rate | 0.4599 |
| gross_profit_factor | 0.8577 |
| gross_win_rate | 0.4599 |
| sharpe_ratio | -2.5035 |
| sortino_ratio | -0.6977 |
| max_drawdown | 0.5668 |
| cagr | -0.2744 |
| net_avg_win | 65.3231 |
| net_avg_loss | -82.1783 |
| avg_hold_time_bars | 14.5194 |
| exposure | 0.2543 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
