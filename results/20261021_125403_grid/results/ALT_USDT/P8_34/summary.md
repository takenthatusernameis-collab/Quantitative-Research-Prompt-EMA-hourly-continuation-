# EMA Hourly Continuation — ALT/USDT P8_34

**Symbol:** ALT/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 774 |
| net_profit_factor | 0.6921 |
| net_win_rate | 0.4716 |
| gross_profit_factor | 0.8932 |
| gross_win_rate | 0.4716 |
| sharpe_ratio | -3.3551 |
| sortino_ratio | -1.3294 |
| max_drawdown | 0.7944 |
| cagr | -0.4572 |
| net_avg_win | 48.3109 |
| net_avg_loss | -62.2929 |
| avg_hold_time_bars | 9.5620 |
| exposure | 0.3364 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
