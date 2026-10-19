# EMA Hourly Continuation — NFT/USDT P100_144

**Symbol:** NFT/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 961 |
| net_profit_factor | 0.1720 |
| net_win_rate | 0.1998 |
| gross_profit_factor | 0.6204 |
| gross_win_rate | 0.2601 |
| sharpe_ratio | -18.7563 |
| sortino_ratio | -9.2605 |
| max_drawdown | 1.0000 |
| cagr | -0.9941 |
| net_avg_win | 10.8225 |
| net_avg_loss | -15.7060 |
| avg_hold_time_bars | 3.7149 |
| exposure | 0.1623 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
