# EMA Hourly Continuation — GRT/USDT P8_89

**Symbol:** GRT/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 747 |
| net_profit_factor | 0.6258 |
| net_win_rate | 0.4779 |
| gross_profit_factor | 0.9382 |
| gross_win_rate | 0.4886 |
| sharpe_ratio | -4.1564 |
| sortino_ratio | -1.5950 |
| max_drawdown | 0.8606 |
| cagr | -0.5355 |
| net_avg_win | 40.0791 |
| net_avg_loss | -58.6223 |
| avg_hold_time_bars | 18.3066 |
| exposure | 0.6188 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
