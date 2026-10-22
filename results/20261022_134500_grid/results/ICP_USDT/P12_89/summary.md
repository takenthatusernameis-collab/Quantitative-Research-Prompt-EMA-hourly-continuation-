# EMA Hourly Continuation — ICP/USDT P12_89

**Symbol:** ICP/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 664 |
| net_profit_factor | 0.5766 |
| net_win_rate | 0.4714 |
| gross_profit_factor | 0.8749 |
| gross_win_rate | 0.4729 |
| sharpe_ratio | -4.2202 |
| sortino_ratio | -1.5226 |
| max_drawdown | 0.8477 |
| cagr | -0.5216 |
| net_avg_win | 36.6834 |
| net_avg_loss | -56.7294 |
| avg_hold_time_bars | 19.2666 |
| exposure | 0.5815 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
