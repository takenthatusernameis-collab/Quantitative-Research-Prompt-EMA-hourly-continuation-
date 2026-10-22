# EMA Hourly Continuation — ACE/USDT P20_34

**Symbol:** ACE/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 452 |
| net_profit_factor | 0.6321 |
| net_win_rate | 0.4889 |
| gross_profit_factor | 0.9171 |
| gross_win_rate | 0.4889 |
| sharpe_ratio | -2.7721 |
| sortino_ratio | -0.8426 |
| max_drawdown | 0.6372 |
| cagr | -0.3195 |
| net_avg_win | 48.3111 |
| net_avg_loss | -73.1160 |
| avg_hold_time_bars | 6.8673 |
| exposure | 0.1405 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
