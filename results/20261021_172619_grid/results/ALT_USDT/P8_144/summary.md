# EMA Hourly Continuation — ALT/USDT P8_144

**Symbol:** ALT/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 421 |
| net_profit_factor | 0.7055 |
| net_win_rate | 0.4632 |
| gross_profit_factor | 0.8467 |
| gross_win_rate | 0.4632 |
| sharpe_ratio | -2.1722 |
| sortino_ratio | -0.6325 |
| max_drawdown | 0.5414 |
| cagr | -0.2534 |
| net_avg_win | 63.8637 |
| net_avg_loss | -78.1111 |
| avg_hold_time_bars | 37.1069 |
| exposure | 0.7101 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
