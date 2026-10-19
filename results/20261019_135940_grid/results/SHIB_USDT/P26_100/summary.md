# EMA Hourly Continuation — SHIB/USDT P26_100

**Symbol:** SHIB/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 666 |
| net_profit_factor | 0.5990 |
| net_win_rate | 0.4685 |
| gross_profit_factor | 0.9933 |
| gross_win_rate | 0.4745 |
| sharpe_ratio | -4.9355 |
| sortino_ratio | -1.7830 |
| max_drawdown | 0.8924 |
| cagr | -0.5834 |
| net_avg_win | 42.5618 |
| net_avg_loss | -62.6274 |
| avg_hold_time_bars | 10.6817 |
| exposure | 0.3234 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
