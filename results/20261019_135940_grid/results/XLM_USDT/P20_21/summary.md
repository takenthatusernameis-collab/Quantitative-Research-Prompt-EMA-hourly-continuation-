# EMA Hourly Continuation — XLM/USDT P20_21

**Symbol:** XLM/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1250 |
| net_profit_factor | 0.0596 |
| net_win_rate | 0.2608 |
| gross_profit_factor | 0.5934 |
| gross_win_rate | 0.3584 |
| sharpe_ratio | -20.2191 |
| sortino_ratio | -11.4323 |
| max_drawdown | 1.0000 |
| cagr | -0.9985 |
| net_avg_win | 1.9440 |
| net_avg_loss | -11.5084 |
| avg_hold_time_bars | 1.5480 |
| exposure | 0.0880 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
