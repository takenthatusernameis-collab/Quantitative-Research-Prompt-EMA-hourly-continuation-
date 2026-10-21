# EMA Hourly Continuation — ENA/USDT P12_26

**Symbol:** ENA/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 393 |
| net_profit_factor | 0.9299 |
| net_win_rate | 0.5420 |
| gross_profit_factor | 1.1670 |
| gross_win_rate | 0.5420 |
| sharpe_ratio | -0.3695 |
| sortino_ratio | -0.1062 |
| max_drawdown | 0.2076 |
| cagr | -0.0525 |
| net_avg_win | 78.9525 |
| net_avg_loss | -100.4681 |
| avg_hold_time_bars | 5.7252 |
| exposure | 0.1023 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
