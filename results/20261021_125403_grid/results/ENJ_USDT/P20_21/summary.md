# EMA Hourly Continuation — ENJ/USDT P20_21

**Symbol:** ENJ/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 139 |
| net_profit_factor | 0.6745 |
| net_win_rate | 0.4964 |
| gross_profit_factor | 0.9866 |
| gross_win_rate | 0.4964 |
| sharpe_ratio | -1.4528 |
| sortino_ratio | -0.2451 |
| max_drawdown | 0.2759 |
| cagr | -0.1070 |
| net_avg_win | 74.5496 |
| net_avg_loss | -108.9526 |
| avg_hold_time_bars | 4.2086 |
| exposure | 0.0265 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
