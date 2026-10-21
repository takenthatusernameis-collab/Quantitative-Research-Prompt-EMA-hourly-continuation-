# EMA Hourly Continuation — SUI/USDT P12_26

**Symbol:** SUI/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 383 |
| net_profit_factor | 0.7269 |
| net_win_rate | 0.4935 |
| gross_profit_factor | 0.9684 |
| gross_win_rate | 0.4935 |
| sharpe_ratio | -1.9590 |
| sortino_ratio | -0.5496 |
| max_drawdown | 0.4810 |
| cagr | -0.2222 |
| net_avg_win | 65.8935 |
| net_avg_loss | -88.3151 |
| avg_hold_time_bars | 5.8668 |
| exposure | 0.1021 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
