# EMA Hourly Continuation — XPR/USDT P21_34

**Symbol:** XPR/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 969 |
| net_profit_factor | 0.2391 |
| net_win_rate | 0.3529 |
| gross_profit_factor | 0.6203 |
| gross_win_rate | 0.3725 |
| sharpe_ratio | -13.4184 |
| sortino_ratio | -6.0661 |
| max_drawdown | 0.9998 |
| cagr | -0.9649 |
| net_avg_win | 9.1883 |
| net_avg_loss | -20.9572 |
| avg_hold_time_bars | 3.5304 |
| exposure | 0.1555 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
