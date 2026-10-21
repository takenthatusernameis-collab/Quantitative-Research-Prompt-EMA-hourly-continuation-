# EMA Hourly Continuation — NFT/USDT P21_26

**Symbol:** NFT/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 219 |
| net_profit_factor | 0.1754 |
| net_win_rate | 0.1872 |
| gross_profit_factor | 0.3643 |
| gross_win_rate | 0.1963 |
| sharpe_ratio | -8.1369 |
| sortino_ratio | -1.8442 |
| max_drawdown | 0.9027 |
| cagr | -0.6045 |
| net_avg_win | 46.8391 |
| net_avg_loss | -61.5012 |
| avg_hold_time_bars | 6.4932 |
| exposure | 0.0646 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
