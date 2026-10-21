# EMA Hourly Continuation — SNX/USDT P12_26

**Symbol:** SNX/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 484 |
| net_profit_factor | 0.8019 |
| net_win_rate | 0.5269 |
| gross_profit_factor | 1.1174 |
| gross_win_rate | 0.5269 |
| sharpe_ratio | -1.5561 |
| sortino_ratio | -0.4935 |
| max_drawdown | 0.4454 |
| cagr | -0.2020 |
| net_avg_win | 68.8806 |
| net_avg_loss | -95.6542 |
| avg_hold_time_bars | 5.6384 |
| exposure | 0.1235 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
