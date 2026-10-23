# EMA Hourly Continuation — ONT/USDT P21_144

**Symbol:** ONT/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 495 |
| net_profit_factor | 0.6451 |
| net_win_rate | 0.4788 |
| gross_profit_factor | 0.8923 |
| gross_win_rate | 0.4828 |
| sharpe_ratio | -2.7090 |
| sortino_ratio | -0.8523 |
| max_drawdown | 0.6442 |
| cagr | -0.3286 |
| net_avg_win | 48.6165 |
| net_avg_loss | -69.2325 |
| avg_hold_time_bars | 23.7778 |
| exposure | 0.5326 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
