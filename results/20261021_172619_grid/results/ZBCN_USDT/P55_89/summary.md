# EMA Hourly Continuation — ZBCN/USDT P55_89

**Symbol:** ZBCN/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 225 |
| net_profit_factor | 0.8333 |
| net_win_rate | 0.5111 |
| gross_profit_factor | 1.0278 |
| gross_win_rate | 0.5111 |
| sharpe_ratio | -0.7859 |
| sortino_ratio | -0.1709 |
| max_drawdown | 0.2501 |
| cagr | -0.0765 |
| net_avg_win | 77.5247 |
| net_avg_loss | -97.2649 |
| avg_hold_time_bars | 5.3067 |
| exposure | 0.0552 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
