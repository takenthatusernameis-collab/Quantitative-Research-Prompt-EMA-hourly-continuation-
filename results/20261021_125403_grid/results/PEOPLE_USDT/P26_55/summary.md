# EMA Hourly Continuation — PEOPLE/USDT P26_55

**Symbol:** PEOPLE/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 493 |
| net_profit_factor | 0.6963 |
| net_win_rate | 0.4828 |
| gross_profit_factor | 0.9169 |
| gross_win_rate | 0.4828 |
| sharpe_ratio | -2.4993 |
| sortino_ratio | -0.7912 |
| max_drawdown | 0.6083 |
| cagr | -0.3041 |
| net_avg_win | 57.7255 |
| net_avg_loss | -77.3767 |
| avg_hold_time_bars | 6.7586 |
| exposure | 0.1508 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
