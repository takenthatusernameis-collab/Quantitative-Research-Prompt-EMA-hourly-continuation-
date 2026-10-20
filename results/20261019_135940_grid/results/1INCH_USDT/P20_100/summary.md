# EMA Hourly Continuation — 1INCH/USDT P20_100

**Symbol:** 1INCH/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 621 |
| net_profit_factor | 0.4990 |
| net_win_rate | 0.4332 |
| gross_profit_factor | 0.8278 |
| gross_win_rate | 0.4461 |
| sharpe_ratio | -5.6590 |
| sortino_ratio | -1.9762 |
| max_drawdown | 0.9149 |
| cagr | -0.6210 |
| net_avg_win | 33.7933 |
| net_avg_loss | -51.7486 |
| avg_hold_time_bars | 17.4944 |
| exposure | 0.4938 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
