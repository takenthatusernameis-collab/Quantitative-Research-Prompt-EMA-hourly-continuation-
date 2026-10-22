# EMA Hourly Continuation — DCR/USDT P8_12

**Symbol:** DCR/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1741 |
| net_profit_factor | 0.1913 |
| net_win_rate | 0.3487 |
| gross_profit_factor | 0.5670 |
| gross_win_rate | 0.4107 |
| sharpe_ratio | -17.4636 |
| sortino_ratio | -10.4675 |
| max_drawdown | 1.0000 |
| cagr | -0.9963 |
| net_avg_win | 3.8983 |
| net_avg_loss | -10.9050 |
| avg_hold_time_bars | 2.3354 |
| exposure | 0.1840 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
