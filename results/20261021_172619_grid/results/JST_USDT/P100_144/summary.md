# EMA Hourly Continuation — JST/USDT P100_144

**Symbol:** JST/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 255 |
| net_profit_factor | 0.4592 |
| net_win_rate | 0.4784 |
| gross_profit_factor | 0.9937 |
| gross_win_rate | 0.4941 |
| sharpe_ratio | -3.5829 |
| sortino_ratio | -0.8220 |
| max_drawdown | 0.6317 |
| cagr | -0.3221 |
| net_avg_win | 43.4952 |
| net_avg_loss | -86.8901 |
| avg_hold_time_bars | 7.8157 |
| exposure | 0.0902 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
