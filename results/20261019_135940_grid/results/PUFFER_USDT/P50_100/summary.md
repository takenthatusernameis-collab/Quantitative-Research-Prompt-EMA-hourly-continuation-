# EMA Hourly Continuation — PUFFER/USDT P50_100

**Symbol:** PUFFER/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 472 |
| net_profit_factor | 0.5305 |
| net_win_rate | 0.4386 |
| gross_profit_factor | 0.7928 |
| gross_win_rate | 0.4492 |
| sharpe_ratio | -4.5215 |
| sortino_ratio | -1.5469 |
| max_drawdown | 0.7747 |
| cagr | -0.5171 |
| net_avg_win | 42.0135 |
| net_avg_loss | -61.8648 |
| avg_hold_time_bars | 7.5953 |
| exposure | 0.2029 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
