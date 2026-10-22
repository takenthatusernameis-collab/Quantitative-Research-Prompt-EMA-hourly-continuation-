# EMA Hourly Continuation — FLIP/USDT P55_89

**Symbol:** FLIP/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 284 |
| net_profit_factor | 0.4995 |
| net_win_rate | 0.4331 |
| gross_profit_factor | 0.8145 |
| gross_win_rate | 0.4472 |
| sharpe_ratio | -3.7591 |
| sortino_ratio | -0.8984 |
| max_drawdown | 0.6677 |
| cagr | -0.3457 |
| net_avg_win | 53.1725 |
| net_avg_loss | -81.3312 |
| avg_hold_time_bars | 11.2711 |
| exposure | 0.1455 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
