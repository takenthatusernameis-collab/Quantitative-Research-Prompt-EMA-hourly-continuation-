# EMA Hourly Continuation — IOTX/USDT P50_144

**Symbol:** IOTX/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 517 |
| net_profit_factor | 0.5231 |
| net_win_rate | 0.4565 |
| gross_profit_factor | 0.8235 |
| gross_win_rate | 0.4623 |
| sharpe_ratio | -4.2521 |
| sortino_ratio | -1.3628 |
| max_drawdown | 0.8117 |
| cagr | -0.4790 |
| net_avg_win | 37.4400 |
| net_avg_loss | -60.1091 |
| avg_hold_time_bars | 12.7621 |
| exposure | 0.2999 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
