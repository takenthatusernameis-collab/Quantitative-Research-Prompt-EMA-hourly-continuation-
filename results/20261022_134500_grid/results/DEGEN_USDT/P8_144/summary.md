# EMA Hourly Continuation — DEGEN/USDT P8_144

**Symbol:** DEGEN/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 376 |
| net_profit_factor | 0.8306 |
| net_win_rate | 0.5080 |
| gross_profit_factor | 1.0382 |
| gross_win_rate | 0.5080 |
| sharpe_ratio | -1.2464 |
| sortino_ratio | -0.3422 |
| max_drawdown | 0.4083 |
| cagr | -0.1510 |
| net_avg_win | 86.3826 |
| net_avg_loss | -107.3777 |
| avg_hold_time_bars | 46.0133 |
| exposure | 0.7877 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
