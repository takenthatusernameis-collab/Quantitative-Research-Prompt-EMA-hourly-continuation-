# EMA Hourly Continuation — DODO/USDT P8_100

**Symbol:** DODO/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 527 |
| net_profit_factor | 0.7182 |
| net_win_rate | 0.4611 |
| gross_profit_factor | 0.8697 |
| gross_win_rate | 0.4611 |
| sharpe_ratio | -2.5486 |
| sortino_ratio | -0.8284 |
| max_drawdown | 0.6569 |
| cagr | -0.3174 |
| net_avg_win | 64.8615 |
| net_avg_loss | -77.2694 |
| avg_hold_time_bars | 25.7951 |
| exposure | 0.6151 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
