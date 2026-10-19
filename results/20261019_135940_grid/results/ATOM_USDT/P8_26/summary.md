# EMA Hourly Continuation — ATOM/USDT P8_26

**Symbol:** ATOM/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1539 |
| net_profit_factor | 0.3835 |
| net_win_rate | 0.4353 |
| gross_profit_factor | 0.8758 |
| gross_win_rate | 0.4607 |
| sharpe_ratio | -10.9514 |
| sortino_ratio | -6.0662 |
| max_drawdown | 0.9995 |
| cagr | -0.9517 |
| net_avg_win | 9.2818 |
| net_avg_loss | -18.6580 |
| avg_hold_time_bars | 3.7901 |
| exposure | 0.2651 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
