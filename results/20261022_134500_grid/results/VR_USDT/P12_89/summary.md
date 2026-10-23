# EMA Hourly Continuation — VR/USDT P12_89

**Symbol:** VR/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 776 |
| net_profit_factor | 0.4834 |
| net_win_rate | 0.3969 |
| gross_profit_factor | 0.7116 |
| gross_win_rate | 0.4059 |
| sharpe_ratio | -7.9588 |
| sortino_ratio | -3.0216 |
| max_drawdown | 0.9848 |
| cagr | -0.8097 |
| net_avg_win | 29.9101 |
| net_avg_loss | -40.7206 |
| avg_hold_time_bars | 14.3505 |
| exposure | 0.5062 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
