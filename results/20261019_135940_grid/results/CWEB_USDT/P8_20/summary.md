# EMA Hourly Continuation — CWEB/USDT P8_20

**Symbol:** CWEB/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1584 |
| net_profit_factor | 0.2656 |
| net_win_rate | 0.2487 |
| gross_profit_factor | 0.7351 |
| gross_win_rate | 0.2835 |
| sharpe_ratio | -21.3289 |
| sortino_ratio | -12.6875 |
| max_drawdown | 1.0000 |
| cagr | -0.9992 |
| net_avg_win | 9.1793 |
| net_avg_loss | -11.4426 |
| avg_hold_time_bars | 4.0619 |
| exposure | 0.2925 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
