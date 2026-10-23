# EMA Hourly Continuation — TURBO/USDT P8_100

**Symbol:** TURBO/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 622 |
| net_profit_factor | 0.6509 |
| net_win_rate | 0.4646 |
| gross_profit_factor | 0.8889 |
| gross_win_rate | 0.4662 |
| sharpe_ratio | -4.1995 |
| sortino_ratio | -1.6151 |
| max_drawdown | 0.8117 |
| cagr | -0.5356 |
| net_avg_win | 51.5530 |
| net_avg_loss | -68.7371 |
| avg_hold_time_bars | 18.1543 |
| exposure | 0.6160 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
