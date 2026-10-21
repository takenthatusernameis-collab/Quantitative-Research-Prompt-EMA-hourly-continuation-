# EMA Hourly Continuation — DASH/USDT P26_55

**Symbol:** DASH/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 394 |
| net_profit_factor | 0.8171 |
| net_win_rate | 0.5305 |
| gross_profit_factor | 1.1426 |
| gross_win_rate | 0.5305 |
| sharpe_ratio | -1.2700 |
| sortino_ratio | -0.3641 |
| max_drawdown | 0.4081 |
| cagr | -0.1544 |
| net_avg_win | 73.4443 |
| net_avg_loss | -101.5507 |
| avg_hold_time_bars | 7.7310 |
| exposure | 0.1385 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
