# EMA Hourly Continuation — WAVES/USDT P8_26

**Symbol:** WAVES/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 672 |
| net_profit_factor | 0.6276 |
| net_win_rate | 0.4821 |
| gross_profit_factor | 0.9221 |
| gross_win_rate | 0.4821 |
| sharpe_ratio | -3.9241 |
| sortino_ratio | -1.4561 |
| max_drawdown | 0.8199 |
| cagr | -0.4886 |
| net_avg_win | 42.3649 |
| net_avg_loss | -62.8438 |
| avg_hold_time_bars | 6.5833 |
| exposure | 0.2011 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
