# EMA Hourly Continuation — WAVES/USDT P55_89

**Symbol:** WAVES/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 330 |
| net_profit_factor | 0.6406 |
| net_win_rate | 0.4970 |
| gross_profit_factor | 0.9393 |
| gross_win_rate | 0.4970 |
| sharpe_ratio | -2.3034 |
| sortino_ratio | -0.6006 |
| max_drawdown | 0.5437 |
| cagr | -0.2412 |
| net_avg_win | 54.3495 |
| net_avg_loss | -83.8148 |
| avg_hold_time_bars | 7.8758 |
| exposure | 0.1181 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
