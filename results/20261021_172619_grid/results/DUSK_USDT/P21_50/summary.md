# EMA Hourly Continuation — DUSK/USDT P21_50

**Symbol:** DUSK/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 520 |
| net_profit_factor | 0.7016 |
| net_win_rate | 0.4635 |
| gross_profit_factor | 0.9008 |
| gross_win_rate | 0.4635 |
| sharpe_ratio | -2.8443 |
| sortino_ratio | -0.9234 |
| max_drawdown | 0.7071 |
| cagr | -0.3462 |
| net_avg_win | 64.0017 |
| net_avg_loss | -78.7999 |
| avg_hold_time_bars | 6.7404 |
| exposure | 0.1593 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
