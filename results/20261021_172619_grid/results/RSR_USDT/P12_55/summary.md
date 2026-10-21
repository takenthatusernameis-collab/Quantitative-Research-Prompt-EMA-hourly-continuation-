# EMA Hourly Continuation — RSR/USDT P12_55

**Symbol:** RSR/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 663 |
| net_profit_factor | 0.7887 |
| net_win_rate | 0.4887 |
| gross_profit_factor | 0.9681 |
| gross_win_rate | 0.4887 |
| sharpe_ratio | -2.0870 |
| sortino_ratio | -0.7678 |
| max_drawdown | 0.6243 |
| cagr | -0.2986 |
| net_avg_win | 67.9305 |
| net_avg_loss | -82.3173 |
| avg_hold_time_bars | 11.1463 |
| exposure | 0.3359 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
