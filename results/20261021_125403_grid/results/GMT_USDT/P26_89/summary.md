# EMA Hourly Continuation — GMT/USDT P26_89

**Symbol:** GMT/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 484 |
| net_profit_factor | 0.6326 |
| net_win_rate | 0.4401 |
| gross_profit_factor | 0.8063 |
| gross_win_rate | 0.4401 |
| sharpe_ratio | -3.3302 |
| sortino_ratio | -1.0391 |
| max_drawdown | 0.7149 |
| cagr | -0.3799 |
| net_avg_win | 56.4969 |
| net_avg_loss | -70.1945 |
| avg_hold_time_bars | 12.5847 |
| exposure | 0.2769 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
