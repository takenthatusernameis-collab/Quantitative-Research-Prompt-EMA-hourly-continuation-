# EMA Hourly Continuation — INJ/USDT P12_100

**Symbol:** INJ/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 660 |
| net_profit_factor | 0.6370 |
| net_win_rate | 0.4636 |
| gross_profit_factor | 0.9009 |
| gross_win_rate | 0.4682 |
| sharpe_ratio | -3.7902 |
| sortino_ratio | -1.3667 |
| max_drawdown | 0.8071 |
| cagr | -0.4787 |
| net_avg_win | 46.1745 |
| net_avg_loss | -62.6613 |
| avg_hold_time_bars | 19.2076 |
| exposure | 0.5762 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
