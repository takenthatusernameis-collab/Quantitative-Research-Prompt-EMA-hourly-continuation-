# EMA Hourly Continuation — SEI/USDT P8_20

**Symbol:** SEI/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 466 |
| net_profit_factor | 0.7776 |
| net_win_rate | 0.5086 |
| gross_profit_factor | 1.0445 |
| gross_win_rate | 0.5086 |
| sharpe_ratio | -1.8316 |
| sortino_ratio | -0.5684 |
| max_drawdown | 0.5392 |
| cagr | -0.2296 |
| net_avg_win | 70.9122 |
| net_avg_loss | -94.3788 |
| avg_hold_time_bars | 6.0021 |
| exposure | 0.1271 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
