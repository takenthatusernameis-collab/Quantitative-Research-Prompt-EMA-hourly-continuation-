# EMA Hourly Continuation — DODO/USDT P8_21

**Symbol:** DODO/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1693 |
| net_profit_factor | 0.3853 |
| net_win_rate | 0.4229 |
| gross_profit_factor | 0.8094 |
| gross_win_rate | 0.4424 |
| sharpe_ratio | -11.5211 |
| sortino_ratio | -6.6673 |
| max_drawdown | 0.9998 |
| cagr | -0.9636 |
| net_avg_win | 8.7512 |
| net_avg_loss | -16.6464 |
| avg_hold_time_bars | 3.4194 |
| exposure | 0.2620 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
