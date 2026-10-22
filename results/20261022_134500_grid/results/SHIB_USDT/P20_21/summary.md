# EMA Hourly Continuation — SHIB/USDT P20_21

**Symbol:** SHIB/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1149 |
| net_profit_factor | 0.0883 |
| net_win_rate | 0.2515 |
| gross_profit_factor | 0.5727 |
| gross_win_rate | 0.3420 |
| sharpe_ratio | -19.6052 |
| sortino_ratio | -10.7265 |
| max_drawdown | 1.0000 |
| cagr | -0.9979 |
| net_avg_win | 3.3501 |
| net_avg_loss | -12.7537 |
| avg_hold_time_bars | 1.5030 |
| exposure | 0.0785 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
