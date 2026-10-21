# EMA Hourly Continuation — XRP/USDT P100_144

**Symbol:** XRP/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 190 |
| net_profit_factor | 0.7627 |
| net_win_rate | 0.5474 |
| gross_profit_factor | 1.2089 |
| gross_win_rate | 0.5474 |
| sharpe_ratio | -1.0978 |
| sortino_ratio | -0.2197 |
| max_drawdown | 0.2245 |
| cagr | -0.0949 |
| net_avg_win | 68.5034 |
| net_avg_loss | -108.6104 |
| avg_hold_time_bars | 7.0053 |
| exposure | 0.0605 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
