# EMA Hourly Continuation — SKL/USDT P8_89

**Symbol:** SKL/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 687 |
| net_profit_factor | 0.7175 |
| net_win_rate | 0.4964 |
| gross_profit_factor | 1.0250 |
| gross_win_rate | 0.5051 |
| sharpe_ratio | -2.9932 |
| sortino_ratio | -1.1102 |
| max_drawdown | 0.7604 |
| cagr | -0.4079 |
| net_avg_win | 54.5015 |
| net_avg_loss | -74.8643 |
| avg_hold_time_bars | 21.5095 |
| exposure | 0.6717 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
