# EMA Hourly Continuation — LSK/USDT P26_55

**Symbol:** LSK/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 523 |
| net_profit_factor | 0.7071 |
| net_win_rate | 0.5086 |
| gross_profit_factor | 1.0619 |
| gross_win_rate | 0.5086 |
| sharpe_ratio | -2.6758 |
| sortino_ratio | -0.8786 |
| max_drawdown | 0.6532 |
| cagr | -0.3313 |
| net_avg_win | 57.7180 |
| net_avg_loss | -84.4874 |
| avg_hold_time_bars | 6.8910 |
| exposure | 0.1638 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
