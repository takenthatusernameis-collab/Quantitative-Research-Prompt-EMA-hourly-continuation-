# EMA Hourly Continuation — ETH/USDT P20_50

**Symbol:** ETH/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 940 |
| net_profit_factor | 0.3307 |
| net_win_rate | 0.3979 |
| gross_profit_factor | 0.9679 |
| gross_win_rate | 0.4564 |
| sharpe_ratio | -10.7342 |
| sortino_ratio | -4.6918 |
| max_drawdown | 0.9979 |
| cagr | -0.9138 |
| net_avg_win | 13.1821 |
| net_avg_loss | -26.3408 |
| avg_hold_time_bars | 4.9745 |
| exposure | 0.2125 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
