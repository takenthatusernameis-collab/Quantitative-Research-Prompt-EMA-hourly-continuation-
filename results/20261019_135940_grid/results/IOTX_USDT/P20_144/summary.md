# EMA Hourly Continuation — IOTX/USDT P20_144

**Symbol:** IOTX/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 577 |
| net_profit_factor | 0.6058 |
| net_win_rate | 0.4714 |
| gross_profit_factor | 0.8879 |
| gross_win_rate | 0.4835 |
| sharpe_ratio | -3.6250 |
| sortino_ratio | -1.2202 |
| max_drawdown | 0.7806 |
| cagr | -0.4444 |
| net_avg_win | 43.5867 |
| net_avg_loss | -64.1640 |
| avg_hold_time_bars | 19.1213 |
| exposure | 0.5015 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
