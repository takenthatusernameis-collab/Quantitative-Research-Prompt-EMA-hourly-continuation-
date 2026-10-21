# EMA Hourly Continuation — GLM/USDT P20_55

**Symbol:** GLM/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 589 |
| net_profit_factor | 0.6391 |
| net_win_rate | 0.4754 |
| gross_profit_factor | 0.9091 |
| gross_win_rate | 0.4754 |
| sharpe_ratio | -3.5602 |
| sortino_ratio | -1.2324 |
| max_drawdown | 0.7685 |
| cagr | -0.4332 |
| net_avg_win | 48.0445 |
| net_avg_loss | -68.1196 |
| avg_hold_time_bars | 9.3107 |
| exposure | 0.2493 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
