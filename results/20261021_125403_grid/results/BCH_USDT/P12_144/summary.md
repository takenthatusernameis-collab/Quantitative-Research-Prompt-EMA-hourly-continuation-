# EMA Hourly Continuation — BCH/USDT P12_144

**Symbol:** BCH/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 368 |
| net_profit_factor | 0.7861 |
| net_win_rate | 0.4946 |
| gross_profit_factor | 0.9977 |
| gross_win_rate | 0.4946 |
| sharpe_ratio | -1.6110 |
| sortino_ratio | -0.4418 |
| max_drawdown | 0.4715 |
| cagr | -0.1848 |
| net_avg_win | 81.0444 |
| net_avg_loss | -100.8813 |
| avg_hold_time_bars | 37.2310 |
| exposure | 0.6228 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
