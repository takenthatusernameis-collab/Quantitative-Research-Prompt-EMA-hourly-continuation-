# EMA Hourly Continuation — ETH/USDT P12_21

**Symbol:** ETH/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1423 |
| net_profit_factor | 0.1736 |
| net_win_rate | 0.3359 |
| gross_profit_factor | 0.7343 |
| gross_win_rate | 0.4153 |
| sharpe_ratio | -17.8951 |
| sortino_ratio | -10.0911 |
| max_drawdown | 1.0000 |
| cagr | -0.9962 |
| net_avg_win | 4.3941 |
| net_avg_loss | -12.8046 |
| avg_hold_time_bars | 2.3197 |
| exposure | 0.1500 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
