# EMA Hourly Continuation — YFI/USDT P12_100

**Symbol:** YFI/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 535 |
| net_profit_factor | 0.6871 |
| net_win_rate | 0.4841 |
| gross_profit_factor | 0.9499 |
| gross_win_rate | 0.4841 |
| sharpe_ratio | -2.7990 |
| sortino_ratio | -0.9221 |
| max_drawdown | 0.6786 |
| cagr | -0.3472 |
| net_avg_win | 55.8839 |
| net_avg_loss | -76.3178 |
| avg_hold_time_bars | 23.5065 |
| exposure | 0.5691 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
