# EMA Hourly Continuation — GTC/USDT P50_144

**Symbol:** GTC/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 373 |
| net_profit_factor | 0.6912 |
| net_win_rate | 0.4665 |
| gross_profit_factor | 0.8708 |
| gross_win_rate | 0.4665 |
| sharpe_ratio | -2.2584 |
| sortino_ratio | -0.6196 |
| max_drawdown | 0.5414 |
| cagr | -0.2483 |
| net_avg_win | 65.8332 |
| net_avg_loss | -83.2768 |
| avg_hold_time_bars | 17.7882 |
| exposure | 0.3016 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
