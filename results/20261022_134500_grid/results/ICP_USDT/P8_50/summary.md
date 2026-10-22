# EMA Hourly Continuation — ICP/USDT P8_50

**Symbol:** ICP/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1184 |
| net_profit_factor | 0.5622 |
| net_win_rate | 0.4637 |
| gross_profit_factor | 0.9123 |
| gross_win_rate | 0.4780 |
| sharpe_ratio | -6.7848 |
| sortino_ratio | -3.2661 |
| max_drawdown | 0.9835 |
| cagr | -0.7988 |
| net_avg_win | 22.9775 |
| net_avg_loss | -35.3329 |
| avg_hold_time_bars | 8.0144 |
| exposure | 0.4313 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
