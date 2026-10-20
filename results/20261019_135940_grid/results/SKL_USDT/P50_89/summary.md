# EMA Hourly Continuation — SKL/USDT P50_89

**Symbol:** SKL/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 695 |
| net_profit_factor | 0.6121 |
| net_win_rate | 0.4950 |
| gross_profit_factor | 1.0418 |
| gross_win_rate | 0.5065 |
| sharpe_ratio | -4.3512 |
| sortino_ratio | -1.6193 |
| max_drawdown | 0.8642 |
| cagr | -0.5402 |
| net_avg_win | 39.3466 |
| net_avg_loss | -63.0042 |
| avg_hold_time_bars | 4.7799 |
| exposure | 0.1510 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
