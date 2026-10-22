# EMA Hourly Continuation — EWT/USDT P8_34

**Symbol:** EWT/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 609 |
| net_profit_factor | 0.5929 |
| net_win_rate | 0.4384 |
| gross_profit_factor | 0.7723 |
| gross_win_rate | 0.4384 |
| sharpe_ratio | -4.0354 |
| sortino_ratio | -1.4129 |
| max_drawdown | 0.8051 |
| cagr | -0.4785 |
| net_avg_win | 43.9114 |
| net_avg_loss | -57.8214 |
| avg_hold_time_bars | 8.5550 |
| exposure | 0.2368 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
