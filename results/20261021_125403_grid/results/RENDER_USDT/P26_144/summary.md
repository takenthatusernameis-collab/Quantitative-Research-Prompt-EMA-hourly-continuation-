# EMA Hourly Continuation — RENDER/USDT P26_144

**Symbol:** RENDER/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 296 |
| net_profit_factor | 0.8820 |
| net_win_rate | 0.5135 |
| gross_profit_factor | 1.0451 |
| gross_win_rate | 0.5135 |
| sharpe_ratio | -0.7250 |
| sortino_ratio | -0.1927 |
| max_drawdown | 0.2814 |
| cagr | -0.0880 |
| net_avg_win | 88.8029 |
| net_avg_loss | -106.2780 |
| avg_hold_time_bars | 29.9797 |
| exposure | 0.4684 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
