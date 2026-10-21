# EMA Hourly Continuation — TRB/USDT P55_89

**Symbol:** TRB/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 316 |
| net_profit_factor | 0.6845 |
| net_win_rate | 0.4810 |
| gross_profit_factor | 0.9386 |
| gross_win_rate | 0.4810 |
| sharpe_ratio | -2.2266 |
| sortino_ratio | -0.5652 |
| max_drawdown | 0.5123 |
| cagr | -0.2277 |
| net_avg_win | 68.3566 |
| net_avg_loss | -92.5530 |
| avg_hold_time_bars | 7.5095 |
| exposure | 0.1074 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
