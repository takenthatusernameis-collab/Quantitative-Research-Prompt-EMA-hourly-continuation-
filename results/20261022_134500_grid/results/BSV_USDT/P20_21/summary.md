# EMA Hourly Continuation — BSV/USDT P20_21

**Symbol:** BSV/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1341 |
| net_profit_factor | 0.0872 |
| net_win_rate | 0.2453 |
| gross_profit_factor | 0.5179 |
| gross_win_rate | 0.3609 |
| sharpe_ratio | -21.0645 |
| sortino_ratio | -12.3019 |
| max_drawdown | 1.0000 |
| cagr | -0.9990 |
| net_avg_win | 2.9049 |
| net_avg_loss | -10.8258 |
| avg_hold_time_bars | 1.8352 |
| exposure | 0.1119 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
