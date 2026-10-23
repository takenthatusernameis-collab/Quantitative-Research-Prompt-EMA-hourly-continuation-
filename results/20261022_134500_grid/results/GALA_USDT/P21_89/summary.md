# EMA Hourly Continuation — GALA/USDT P21_89

**Symbol:** GALA/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 709 |
| net_profit_factor | 0.5974 |
| net_win_rate | 0.4626 |
| gross_profit_factor | 0.8671 |
| gross_win_rate | 0.4697 |
| sharpe_ratio | -4.4174 |
| sortino_ratio | -1.6612 |
| max_drawdown | 0.8693 |
| cagr | -0.5444 |
| net_avg_win | 38.9520 |
| net_avg_loss | -56.1360 |
| avg_hold_time_bars | 12.2031 |
| exposure | 0.3933 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
