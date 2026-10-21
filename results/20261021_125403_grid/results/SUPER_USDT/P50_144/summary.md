# EMA Hourly Continuation — SUPER/USDT P50_144

**Symbol:** SUPER/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 343 |
| net_profit_factor | 0.8090 |
| net_win_rate | 0.5102 |
| gross_profit_factor | 1.0075 |
| gross_win_rate | 0.5102 |
| sharpe_ratio | -1.0838 |
| sortino_ratio | -0.2879 |
| max_drawdown | 0.3587 |
| cagr | -0.1251 |
| net_avg_win | 69.0445 |
| net_avg_loss | -88.8963 |
| avg_hold_time_bars | 17.5423 |
| exposure | 0.2735 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
