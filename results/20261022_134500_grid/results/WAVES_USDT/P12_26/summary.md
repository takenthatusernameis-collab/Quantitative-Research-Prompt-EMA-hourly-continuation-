# EMA Hourly Continuation — WAVES/USDT P12_26

**Symbol:** WAVES/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1544 |
| net_profit_factor | 0.3596 |
| net_win_rate | 0.3912 |
| gross_profit_factor | 0.9165 |
| gross_win_rate | 0.4437 |
| sharpe_ratio | -13.9781 |
| sortino_ratio | -7.8250 |
| max_drawdown | 1.0000 |
| cagr | -0.9829 |
| net_avg_win | 9.2981 |
| net_avg_loss | -16.6124 |
| avg_hold_time_bars | 3.0408 |
| exposure | 0.2134 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
