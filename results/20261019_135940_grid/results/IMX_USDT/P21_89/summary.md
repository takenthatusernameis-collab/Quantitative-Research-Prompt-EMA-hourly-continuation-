# EMA Hourly Continuation — IMX/USDT P21_89

**Symbol:** IMX/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 665 |
| net_profit_factor | 0.6610 |
| net_win_rate | 0.4887 |
| gross_profit_factor | 0.9490 |
| gross_win_rate | 0.4932 |
| sharpe_ratio | -3.1533 |
| sortino_ratio | -1.1470 |
| max_drawdown | 0.7503 |
| cagr | -0.4193 |
| net_avg_win | 44.7781 |
| net_avg_loss | -64.7494 |
| avg_hold_time_bars | 12.9850 |
| exposure | 0.3907 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
