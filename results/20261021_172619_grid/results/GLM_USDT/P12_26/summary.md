# EMA Hourly Continuation — GLM/USDT P12_26

**Symbol:** GLM/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 653 |
| net_profit_factor | 0.6477 |
| net_win_rate | 0.4977 |
| gross_profit_factor | 1.0034 |
| gross_win_rate | 0.4977 |
| sharpe_ratio | -3.7627 |
| sortino_ratio | -1.3839 |
| max_drawdown | 0.7977 |
| cagr | -0.4681 |
| net_avg_win | 44.9749 |
| net_avg_loss | -68.8047 |
| avg_hold_time_bars | 5.5161 |
| exposure | 0.1637 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
