# EMA Hourly Continuation — MANTA/USDT P21_26

**Symbol:** MANTA/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 227 |
| net_profit_factor | 0.5511 |
| net_win_rate | 0.4361 |
| gross_profit_factor | 0.7873 |
| gross_win_rate | 0.4361 |
| sharpe_ratio | -2.9708 |
| sortino_ratio | -0.6389 |
| max_drawdown | 0.5520 |
| cagr | -0.2553 |
| net_avg_win | 64.8644 |
| net_avg_loss | -91.0264 |
| avg_hold_time_bars | 5.3084 |
| exposure | 0.0548 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
