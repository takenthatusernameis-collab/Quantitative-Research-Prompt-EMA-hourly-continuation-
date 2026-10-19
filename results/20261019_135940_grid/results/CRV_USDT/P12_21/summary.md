# EMA Hourly Continuation — CRV/USDT P12_21

**Symbol:** CRV/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1470 |
| net_profit_factor | 0.3248 |
| net_win_rate | 0.4388 |
| gross_profit_factor | 0.7816 |
| gross_win_rate | 0.4633 |
| sharpe_ratio | -11.4216 |
| sortino_ratio | -6.1927 |
| max_drawdown | 0.9996 |
| cagr | -0.9577 |
| net_avg_win | 7.4555 |
| net_avg_loss | -17.9458 |
| avg_hold_time_bars | 2.1490 |
| exposure | 0.1436 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
