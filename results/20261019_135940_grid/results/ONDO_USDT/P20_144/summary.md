# EMA Hourly Continuation — ONDO/USDT P20_144

**Symbol:** ONDO/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 546 |
| net_profit_factor | 0.7218 |
| net_win_rate | 0.4908 |
| gross_profit_factor | 1.0119 |
| gross_win_rate | 0.4982 |
| sharpe_ratio | -2.6825 |
| sortino_ratio | -0.8786 |
| max_drawdown | 0.6958 |
| cagr | -0.3437 |
| net_avg_win | 63.1975 |
| net_avg_loss | -84.4046 |
| avg_hold_time_bars | 19.2985 |
| exposure | 0.4790 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
