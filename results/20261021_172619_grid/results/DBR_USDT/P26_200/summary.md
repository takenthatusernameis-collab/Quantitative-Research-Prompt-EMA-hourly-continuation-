# EMA Hourly Continuation — DBR/USDT P26_200

**Symbol:** DBR/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 242 |
| net_profit_factor | 0.6638 |
| net_win_rate | 0.4628 |
| gross_profit_factor | 0.8646 |
| gross_win_rate | 0.4669 |
| sharpe_ratio | -2.1755 |
| sortino_ratio | -0.5373 |
| max_drawdown | 0.4319 |
| cagr | -0.2192 |
| net_avg_win | 69.0189 |
| net_avg_loss | -89.5787 |
| avg_hold_time_bars | 38.1033 |
| exposure | 0.5244 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
