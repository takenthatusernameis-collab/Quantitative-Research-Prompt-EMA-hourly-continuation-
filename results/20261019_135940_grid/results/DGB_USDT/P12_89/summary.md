# EMA Hourly Continuation — DGB/USDT P12_89

**Symbol:** DGB/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 867 |
| net_profit_factor | 0.6340 |
| net_win_rate | 0.4671 |
| gross_profit_factor | 1.0167 |
| gross_win_rate | 0.4856 |
| sharpe_ratio | -5.0041 |
| sortino_ratio | -2.0606 |
| max_drawdown | 0.9228 |
| cagr | -0.6331 |
| net_avg_win | 39.3165 |
| net_avg_loss | -54.3663 |
| avg_hold_time_bars | 13.1580 |
| exposure | 0.5185 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
