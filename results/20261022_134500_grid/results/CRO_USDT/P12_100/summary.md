# EMA Hourly Continuation — CRO/USDT P12_100

**Symbol:** CRO/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 683 |
| net_profit_factor | 0.4633 |
| net_win_rate | 0.4510 |
| gross_profit_factor | 0.8660 |
| gross_win_rate | 0.4656 |
| sharpe_ratio | -5.8306 |
| sortino_ratio | -2.1233 |
| max_drawdown | 0.9365 |
| cagr | -0.6577 |
| net_avg_win | 26.1296 |
| net_avg_loss | -46.3213 |
| avg_hold_time_bars | 18.3367 |
| exposure | 0.5693 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
