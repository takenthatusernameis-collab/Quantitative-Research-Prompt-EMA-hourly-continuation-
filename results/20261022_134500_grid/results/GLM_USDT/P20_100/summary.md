# EMA Hourly Continuation — GLM/USDT P20_100

**Symbol:** GLM/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 669 |
| net_profit_factor | 0.5275 |
| net_win_rate | 0.4410 |
| gross_profit_factor | 0.8085 |
| gross_win_rate | 0.4469 |
| sharpe_ratio | -5.3354 |
| sortino_ratio | -1.9304 |
| max_drawdown | 0.9082 |
| cagr | -0.6104 |
| net_avg_win | 34.3004 |
| net_avg_loss | -51.2872 |
| avg_hold_time_bars | 14.7130 |
| exposure | 0.4474 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
