# EMA Hourly Continuation — GRT/USDT P20_144

**Symbol:** GRT/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 495 |
| net_profit_factor | 0.6949 |
| net_win_rate | 0.4929 |
| gross_profit_factor | 0.9962 |
| gross_win_rate | 0.4990 |
| sharpe_ratio | -2.6212 |
| sortino_ratio | -0.8233 |
| max_drawdown | 0.6529 |
| cagr | -0.3219 |
| net_avg_win | 58.3003 |
| net_avg_loss | -81.5614 |
| avg_hold_time_bars | 23.5778 |
| exposure | 0.5281 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
