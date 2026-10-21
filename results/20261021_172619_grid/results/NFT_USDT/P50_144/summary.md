# EMA Hourly Continuation — NFT/USDT P50_144

**Symbol:** NFT/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 370 |
| net_profit_factor | 0.4038 |
| net_win_rate | 0.3459 |
| gross_profit_factor | 0.6873 |
| gross_win_rate | 0.3486 |
| sharpe_ratio | -6.5945 |
| sortino_ratio | -1.8369 |
| max_drawdown | 0.8896 |
| cagr | -0.5787 |
| net_avg_win | 46.8727 |
| net_avg_loss | -61.3991 |
| avg_hold_time_bars | 16.5324 |
| exposure | 0.2780 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
