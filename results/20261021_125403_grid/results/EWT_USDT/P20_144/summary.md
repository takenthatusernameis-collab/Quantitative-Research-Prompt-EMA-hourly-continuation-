# EMA Hourly Continuation — EWT/USDT P20_144

**Symbol:** EWT/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 438 |
| net_profit_factor | 0.6980 |
| net_win_rate | 0.4589 |
| gross_profit_factor | 0.8338 |
| gross_win_rate | 0.4589 |
| sharpe_ratio | -2.2851 |
| sortino_ratio | -0.6775 |
| max_drawdown | 0.6040 |
| cagr | -0.2685 |
| net_avg_win | 62.5687 |
| net_avg_loss | -76.0185 |
| avg_hold_time_bars | 21.5936 |
| exposure | 0.4299 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
