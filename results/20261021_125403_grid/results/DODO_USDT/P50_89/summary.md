# EMA Hourly Continuation — DODO/USDT P50_89

**Symbol:** DODO/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 400 |
| net_profit_factor | 0.6865 |
| net_win_rate | 0.4700 |
| gross_profit_factor | 0.9274 |
| gross_win_rate | 0.4700 |
| sharpe_ratio | -2.6746 |
| sortino_ratio | -0.7617 |
| max_drawdown | 0.5934 |
| cagr | -0.2945 |
| net_avg_win | 68.1853 |
| net_avg_loss | -88.0742 |
| avg_hold_time_bars | 7.0025 |
| exposure | 0.1267 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
