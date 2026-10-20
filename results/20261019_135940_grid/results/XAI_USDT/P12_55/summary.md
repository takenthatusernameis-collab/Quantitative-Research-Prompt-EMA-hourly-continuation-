# EMA Hourly Continuation — XAI/USDT P12_55

**Symbol:** XAI/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1058 |
| net_profit_factor | 0.6716 |
| net_win_rate | 0.4556 |
| gross_profit_factor | 0.9728 |
| gross_win_rate | 0.4698 |
| sharpe_ratio | -5.8810 |
| sortino_ratio | -2.7016 |
| max_drawdown | 0.9625 |
| cagr | -0.7215 |
| net_avg_win | 40.7180 |
| net_avg_loss | -50.7335 |
| avg_hold_time_bars | 8.5113 |
| exposure | 0.4093 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
