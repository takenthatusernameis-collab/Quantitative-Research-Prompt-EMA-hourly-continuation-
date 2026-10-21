# EMA Hourly Continuation — GTC/USDT P12_20

**Symbol:** GTC/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 423 |
| net_profit_factor | 0.6089 |
| net_win_rate | 0.4704 |
| gross_profit_factor | 0.9002 |
| gross_win_rate | 0.4704 |
| sharpe_ratio | -3.3289 |
| sortino_ratio | -0.9803 |
| max_drawdown | 0.6863 |
| cagr | -0.3615 |
| net_avg_win | 52.8791 |
| net_avg_loss | -77.1497 |
| avg_hold_time_bars | 5.1064 |
| exposure | 0.0982 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
