# EMA Hourly Continuation — NFT/USDT P12_100

**Symbol:** NFT/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 517 |
| net_profit_factor | 0.4852 |
| net_win_rate | 0.3714 |
| gross_profit_factor | 0.7841 |
| gross_win_rate | 0.3733 |
| sharpe_ratio | -6.9914 |
| sortino_ratio | -2.2873 |
| max_drawdown | 0.9351 |
| cagr | -0.6587 |
| net_avg_win | 45.7794 |
| net_avg_loss | -55.7451 |
| avg_hold_time_bars | 18.9923 |
| exposure | 0.4463 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
