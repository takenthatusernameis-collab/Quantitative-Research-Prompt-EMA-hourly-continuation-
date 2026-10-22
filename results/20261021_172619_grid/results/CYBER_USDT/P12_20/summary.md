# EMA Hourly Continuation — CYBER/USDT P12_20

**Symbol:** CYBER/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 455 |
| net_profit_factor | 0.6827 |
| net_win_rate | 0.4989 |
| gross_profit_factor | 1.0090 |
| gross_win_rate | 0.4989 |
| sharpe_ratio | -2.7633 |
| sortino_ratio | -0.8464 |
| max_drawdown | 0.6255 |
| cagr | -0.3213 |
| net_avg_win | 58.9781 |
| net_avg_loss | -86.0071 |
| avg_hold_time_bars | 5.5802 |
| exposure | 0.1154 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
