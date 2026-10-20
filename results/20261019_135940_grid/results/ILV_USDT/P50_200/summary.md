# EMA Hourly Continuation — ILV/USDT P50_200

**Symbol:** ILV/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 329 |
| net_profit_factor | 0.8067 |
| net_win_rate | 0.5198 |
| gross_profit_factor | 1.1130 |
| gross_win_rate | 0.5258 |
| sharpe_ratio | -1.2719 |
| sortino_ratio | -0.3269 |
| max_drawdown | 0.3814 |
| cagr | -0.1452 |
| net_avg_win | 79.4422 |
| net_avg_loss | -106.5864 |
| avg_hold_time_bars | 28.4043 |
| exposure | 0.4248 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
