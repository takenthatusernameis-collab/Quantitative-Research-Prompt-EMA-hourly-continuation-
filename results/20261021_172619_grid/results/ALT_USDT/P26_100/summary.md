# EMA Hourly Continuation — ALT/USDT P26_100

**Symbol:** ALT/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 448 |
| net_profit_factor | 0.8591 |
| net_win_rate | 0.5179 |
| gross_profit_factor | 1.0635 |
| gross_win_rate | 0.5179 |
| sharpe_ratio | -0.9774 |
| sortino_ratio | -0.2974 |
| max_drawdown | 0.3501 |
| cagr | -0.1305 |
| net_avg_win | 77.8255 |
| net_avg_loss | -97.3036 |
| avg_hold_time_bars | 18.6004 |
| exposure | 0.3788 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
