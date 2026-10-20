# EMA Hourly Continuation — NOT/USDT P55_100

**Symbol:** NOT/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 627 |
| net_profit_factor | 0.4960 |
| net_win_rate | 0.4577 |
| gross_profit_factor | 0.8148 |
| gross_win_rate | 0.4641 |
| sharpe_ratio | -5.1943 |
| sortino_ratio | -1.8737 |
| max_drawdown | 0.8883 |
| cagr | -0.5926 |
| net_avg_win | 30.4168 |
| net_avg_loss | -51.7684 |
| avg_hold_time_bars | 4.7400 |
| exposure | 0.1396 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
