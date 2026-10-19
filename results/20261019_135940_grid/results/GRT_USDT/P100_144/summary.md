# EMA Hourly Continuation — GRT/USDT P100_144

**Symbol:** GRT/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 464 |
| net_profit_factor | 0.4540 |
| net_win_rate | 0.4547 |
| gross_profit_factor | 0.8949 |
| gross_win_rate | 0.4720 |
| sharpe_ratio | -5.2838 |
| sortino_ratio | -1.6115 |
| max_drawdown | 0.8698 |
| cagr | -0.5478 |
| net_avg_win | 34.0796 |
| net_avg_loss | -62.6098 |
| avg_hold_time_bars | 3.9375 |
| exposure | 0.0827 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
