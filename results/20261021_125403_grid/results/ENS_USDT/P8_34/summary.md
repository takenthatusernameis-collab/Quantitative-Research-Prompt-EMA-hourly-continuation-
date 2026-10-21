# EMA Hourly Continuation — ENS/USDT P8_34

**Symbol:** ENS/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 747 |
| net_profit_factor | 0.7499 |
| net_win_rate | 0.5007 |
| gross_profit_factor | 0.9870 |
| gross_win_rate | 0.5007 |
| sharpe_ratio | -2.4832 |
| sortino_ratio | -0.9728 |
| max_drawdown | 0.6810 |
| cagr | -0.3606 |
| net_avg_win | 54.0758 |
| net_avg_loss | -72.3087 |
| avg_hold_time_bars | 8.8902 |
| exposure | 0.3019 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
