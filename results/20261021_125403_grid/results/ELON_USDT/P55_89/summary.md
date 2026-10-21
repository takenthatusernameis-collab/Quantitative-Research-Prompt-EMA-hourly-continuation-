# EMA Hourly Continuation — ELON/USDT P55_89

**Symbol:** ELON/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 240 |
| net_profit_factor | 0.6382 |
| net_win_rate | 0.4708 |
| gross_profit_factor | 0.8913 |
| gross_win_rate | 0.4708 |
| sharpe_ratio | -2.2008 |
| sortino_ratio | -0.4878 |
| max_drawdown | 0.4325 |
| cagr | -0.2002 |
| net_avg_win | 67.0187 |
| net_avg_loss | -93.4392 |
| avg_hold_time_bars | 7.3708 |
| exposure | 0.0804 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
