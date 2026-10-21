# EMA Hourly Continuation — BSV/USDT P8_100

**Symbol:** BSV/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 549 |
| net_profit_factor | 0.6750 |
| net_win_rate | 0.4590 |
| gross_profit_factor | 0.8607 |
| gross_win_rate | 0.4590 |
| sharpe_ratio | -3.0421 |
| sortino_ratio | -1.0118 |
| max_drawdown | 0.7082 |
| cagr | -0.3721 |
| net_avg_win | 56.7991 |
| net_avg_loss | -71.4005 |
| avg_hold_time_bars | 25.0820 |
| exposure | 0.6259 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
