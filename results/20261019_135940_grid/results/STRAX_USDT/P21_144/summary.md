# EMA Hourly Continuation — STRAX/USDT P21_144

**Symbol:** STRAX/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 684 |
| net_profit_factor | 0.5489 |
| net_win_rate | 0.4123 |
| gross_profit_factor | 0.7849 |
| gross_win_rate | 0.4196 |
| sharpe_ratio | -6.1035 |
| sortino_ratio | -2.2444 |
| max_drawdown | 0.9354 |
| cagr | -0.6641 |
| net_avg_win | 40.3211 |
| net_avg_loss | -51.5285 |
| avg_hold_time_bars | 14.9722 |
| exposure | 0.4682 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
