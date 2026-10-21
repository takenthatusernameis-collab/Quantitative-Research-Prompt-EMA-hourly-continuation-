# EMA Hourly Continuation — LSK/USDT P12_50

**Symbol:** LSK/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 683 |
| net_profit_factor | 0.7301 |
| net_win_rate | 0.4876 |
| gross_profit_factor | 1.0012 |
| gross_win_rate | 0.4876 |
| sharpe_ratio | -2.9876 |
| sortino_ratio | -1.1172 |
| max_drawdown | 0.7526 |
| cagr | -0.4001 |
| net_avg_win | 58.7270 |
| net_avg_loss | -76.5271 |
| avg_hold_time_bars | 10.3265 |
| exposure | 0.3206 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
