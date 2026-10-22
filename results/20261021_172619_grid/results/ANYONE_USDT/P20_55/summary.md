# EMA Hourly Continuation — ANYONE/USDT P20_55

**Symbol:** ANYONE/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 477 |
| net_profit_factor | 0.6545 |
| net_win_rate | 0.4507 |
| gross_profit_factor | 0.7874 |
| gross_win_rate | 0.4507 |
| sharpe_ratio | -2.8602 |
| sortino_ratio | -0.9322 |
| max_drawdown | 0.6316 |
| cagr | -0.3501 |
| net_avg_win | 54.8276 |
| net_avg_loss | -68.7416 |
| avg_hold_time_bars | 8.2851 |
| exposure | 0.1997 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
