# EMA Hourly Continuation — AGLD/USDT P50_100

**Symbol:** AGLD/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 656 |
| net_profit_factor | 0.5570 |
| net_win_rate | 0.4543 |
| gross_profit_factor | 0.8818 |
| gross_win_rate | 0.4619 |
| sharpe_ratio | -4.9779 |
| sortino_ratio | -1.7984 |
| max_drawdown | 0.8909 |
| cagr | -0.5753 |
| net_avg_win | 37.3196 |
| net_avg_loss | -55.7763 |
| avg_hold_time_bars | 6.2561 |
| exposure | 0.1857 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
