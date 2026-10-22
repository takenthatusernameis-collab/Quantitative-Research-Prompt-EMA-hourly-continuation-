# EMA Hourly Continuation — ICP/USDT P8_144

**Symbol:** ICP/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 445 |
| net_profit_factor | 0.6679 |
| net_win_rate | 0.4831 |
| gross_profit_factor | 0.9530 |
| gross_win_rate | 0.4854 |
| sharpe_ratio | -2.7376 |
| sortino_ratio | -0.8133 |
| max_drawdown | 0.6385 |
| cagr | -0.3213 |
| net_avg_win | 58.1857 |
| net_avg_loss | -81.4391 |
| avg_hold_time_bars | 38.1011 |
| exposure | 0.7707 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
