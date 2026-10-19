# EMA Hourly Continuation — NFT/USDT P34_144

**Symbol:** NFT/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 934 |
| net_profit_factor | 0.2975 |
| net_win_rate | 0.2484 |
| gross_profit_factor | 0.6677 |
| gross_win_rate | 0.2805 |
| sharpe_ratio | -16.1691 |
| sortino_ratio | -7.4664 |
| max_drawdown | 1.0000 |
| cagr | -0.9825 |
| net_avg_win | 18.2554 |
| net_avg_loss | -20.2776 |
| avg_hold_time_bars | 10.3630 |
| exposure | 0.4400 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
