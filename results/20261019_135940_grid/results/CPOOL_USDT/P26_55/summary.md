# EMA Hourly Continuation — CPOOL/USDT P26_55

**Symbol:** CPOOL/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 896 |
| net_profit_factor | 0.5022 |
| net_win_rate | 0.4475 |
| gross_profit_factor | 0.7641 |
| gross_win_rate | 0.4576 |
| sharpe_ratio | -6.3722 |
| sortino_ratio | -2.6590 |
| max_drawdown | 0.9651 |
| cagr | -0.7343 |
| net_avg_win | 24.2547 |
| net_avg_loss | -39.1268 |
| avg_hold_time_bars | 3.8929 |
| exposure | 0.1585 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
