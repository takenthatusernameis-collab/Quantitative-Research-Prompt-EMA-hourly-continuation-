# EMA Hourly Continuation — NYM/USDT P20_200

**Symbol:** NYM/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 278 |
| net_profit_factor | 0.4618 |
| net_win_rate | 0.3705 |
| gross_profit_factor | 0.6194 |
| gross_win_rate | 0.3741 |
| sharpe_ratio | -3.9768 |
| sortino_ratio | -0.9325 |
| max_drawdown | 0.6645 |
| cagr | -0.3527 |
| net_avg_win | 55.3667 |
| net_avg_loss | -70.5585 |
| avg_hold_time_bars | 45.1115 |
| exposure | 0.5700 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
