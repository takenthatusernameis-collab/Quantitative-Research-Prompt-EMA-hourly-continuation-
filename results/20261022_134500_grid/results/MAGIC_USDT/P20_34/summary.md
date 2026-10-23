# EMA Hourly Continuation — MAGIC/USDT P20_34

**Symbol:** MAGIC/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1091 |
| net_profit_factor | 0.5048 |
| net_win_rate | 0.4445 |
| gross_profit_factor | 1.0020 |
| gross_win_rate | 0.4638 |
| sharpe_ratio | -8.6495 |
| sortino_ratio | -4.0396 |
| max_drawdown | 0.9935 |
| cagr | -0.8646 |
| net_avg_win | 20.8788 |
| net_avg_loss | -33.1027 |
| avg_hold_time_bars | 3.5280 |
| exposure | 0.1750 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
