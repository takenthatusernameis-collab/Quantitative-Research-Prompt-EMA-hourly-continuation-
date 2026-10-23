# EMA Hourly Continuation — CATI/USDT P8_20

**Symbol:** CATI/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1435 |
| net_profit_factor | 0.3777 |
| net_win_rate | 0.3742 |
| gross_profit_factor | 0.6664 |
| gross_win_rate | 0.4014 |
| sharpe_ratio | -14.7359 |
| sortino_ratio | -8.6607 |
| max_drawdown | 0.9999 |
| cagr | -0.9887 |
| net_avg_win | 11.2999 |
| net_avg_loss | -17.8922 |
| avg_hold_time_bars | 2.7826 |
| exposure | 0.2189 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
