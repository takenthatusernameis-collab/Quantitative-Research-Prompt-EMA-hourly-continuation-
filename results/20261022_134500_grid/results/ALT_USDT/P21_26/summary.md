# EMA Hourly Continuation — ALT/USDT P21_26

**Symbol:** ALT/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 999 |
| net_profit_factor | 0.3153 |
| net_win_rate | 0.3954 |
| gross_profit_factor | 0.8047 |
| gross_win_rate | 0.4384 |
| sharpe_ratio | -10.6680 |
| sortino_ratio | -4.7847 |
| max_drawdown | 0.9981 |
| cagr | -0.9161 |
| net_avg_win | 11.6364 |
| net_avg_loss | -24.1334 |
| avg_hold_time_bars | 3.0571 |
| exposure | 0.1388 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
