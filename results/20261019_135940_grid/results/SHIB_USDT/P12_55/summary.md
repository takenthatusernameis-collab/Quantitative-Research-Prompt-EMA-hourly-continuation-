# EMA Hourly Continuation — SHIB/USDT P12_55

**Symbol:** SHIB/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1070 |
| net_profit_factor | 0.5471 |
| net_win_rate | 0.4607 |
| gross_profit_factor | 0.9752 |
| gross_win_rate | 0.4785 |
| sharpe_ratio | -7.3708 |
| sortino_ratio | -3.3735 |
| max_drawdown | 0.9869 |
| cagr | -0.8144 |
| net_avg_win | 24.1455 |
| net_avg_loss | -37.7089 |
| avg_hold_time_bars | 7.1654 |
| exposure | 0.3485 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
