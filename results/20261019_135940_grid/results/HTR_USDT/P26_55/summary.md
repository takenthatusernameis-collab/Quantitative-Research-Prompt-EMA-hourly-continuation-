# EMA Hourly Continuation — HTR/USDT P26_55

**Symbol:** HTR/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 900 |
| net_profit_factor | 0.4747 |
| net_win_rate | 0.4067 |
| gross_profit_factor | 0.7758 |
| gross_win_rate | 0.4167 |
| sharpe_ratio | -8.2931 |
| sortino_ratio | -3.5028 |
| max_drawdown | 0.9885 |
| cagr | -0.8255 |
| net_avg_win | 24.3847 |
| net_avg_loss | -35.2062 |
| avg_hold_time_bars | 4.7244 |
| exposure | 0.1933 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
