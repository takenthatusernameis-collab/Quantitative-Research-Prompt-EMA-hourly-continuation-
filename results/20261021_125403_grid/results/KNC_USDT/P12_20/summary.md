# EMA Hourly Continuation — KNC/USDT P12_20

**Symbol:** KNC/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 572 |
| net_profit_factor | 0.5348 |
| net_win_rate | 0.4598 |
| gross_profit_factor | 0.9193 |
| gross_win_rate | 0.4598 |
| sharpe_ratio | -5.3334 |
| sortino_ratio | -1.8302 |
| max_drawdown | 0.8879 |
| cagr | -0.5753 |
| net_avg_win | 38.6297 |
| net_avg_loss | -61.4748 |
| avg_hold_time_bars | 5.2098 |
| exposure | 0.1355 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
