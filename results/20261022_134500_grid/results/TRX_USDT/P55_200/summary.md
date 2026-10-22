# EMA Hourly Continuation — TRX/USDT P55_200

**Symbol:** TRX/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 388 |
| net_profit_factor | 0.3100 |
| net_win_rate | 0.4227 |
| gross_profit_factor | 0.9407 |
| gross_win_rate | 0.4871 |
| sharpe_ratio | -6.4549 |
| sortino_ratio | -1.7963 |
| max_drawdown | 0.9126 |
| cagr | -0.6190 |
| net_avg_win | 24.9615 |
| net_avg_loss | -58.9623 |
| avg_hold_time_bars | 16.5773 |
| exposure | 0.2924 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
