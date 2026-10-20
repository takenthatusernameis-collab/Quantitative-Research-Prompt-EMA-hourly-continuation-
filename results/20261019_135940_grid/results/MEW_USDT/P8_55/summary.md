# EMA Hourly Continuation — MEW/USDT P8_55

**Symbol:** MEW/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 965 |
| net_profit_factor | 0.6477 |
| net_win_rate | 0.4777 |
| gross_profit_factor | 0.9282 |
| gross_win_rate | 0.4850 |
| sharpe_ratio | -4.5989 |
| sortino_ratio | -2.0180 |
| max_drawdown | 0.9107 |
| cagr | -0.6147 |
| net_avg_win | 36.2511 |
| net_avg_loss | -51.1912 |
| avg_hold_time_bars | 11.2311 |
| exposure | 0.4926 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
