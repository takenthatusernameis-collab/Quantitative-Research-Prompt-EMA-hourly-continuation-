# EMA Hourly Continuation — NFT/USDT P12_89

**Symbol:** NFT/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1294 |
| net_profit_factor | 0.2959 |
| net_win_rate | 0.2519 |
| gross_profit_factor | 0.7548 |
| gross_win_rate | 0.2937 |
| sharpe_ratio | -19.1488 |
| sortino_ratio | -10.3675 |
| max_drawdown | 1.0000 |
| cagr | -0.9966 |
| net_avg_win | 12.8941 |
| net_avg_loss | -14.6730 |
| avg_hold_time_bars | 8.2450 |
| exposure | 0.4850 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
