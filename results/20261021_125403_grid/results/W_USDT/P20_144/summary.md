# EMA Hourly Continuation — W/USDT P20_144

**Symbol:** W/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 389 |
| net_profit_factor | 0.9131 |
| net_win_rate | 0.5193 |
| gross_profit_factor | 1.0725 |
| gross_win_rate | 0.5193 |
| sharpe_ratio | -0.5432 |
| sortino_ratio | -0.1539 |
| max_drawdown | 0.2805 |
| cagr | -0.0729 |
| net_avg_win | 90.0109 |
| net_avg_loss | -106.4841 |
| avg_hold_time_bars | 30.1285 |
| exposure | 0.5327 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
