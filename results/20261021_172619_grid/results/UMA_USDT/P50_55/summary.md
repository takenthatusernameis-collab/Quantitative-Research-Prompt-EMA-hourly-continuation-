# EMA Hourly Continuation — UMA/USDT P50_55

**Symbol:** UMA/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 203 |
| net_profit_factor | 0.5669 |
| net_win_rate | 0.4778 |
| gross_profit_factor | 0.9342 |
| gross_win_rate | 0.4778 |
| sharpe_ratio | -2.6269 |
| sortino_ratio | -0.5343 |
| max_drawdown | 0.4720 |
| cagr | -0.2219 |
| net_avg_win | 63.0656 |
| net_avg_loss | -101.8080 |
| avg_hold_time_bars | 5.8522 |
| exposure | 0.0540 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
