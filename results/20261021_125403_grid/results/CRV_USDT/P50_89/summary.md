# EMA Hourly Continuation — CRV/USDT P50_89

**Symbol:** CRV/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 323 |
| net_profit_factor | 0.8041 |
| net_win_rate | 0.5170 |
| gross_profit_factor | 1.0618 |
| gross_win_rate | 0.5170 |
| sharpe_ratio | -1.1957 |
| sortino_ratio | -0.3094 |
| max_drawdown | 0.3303 |
| cagr | -0.1328 |
| net_avg_win | 73.9331 |
| net_avg_loss | -98.4342 |
| avg_hold_time_bars | 7.2879 |
| exposure | 0.1070 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
