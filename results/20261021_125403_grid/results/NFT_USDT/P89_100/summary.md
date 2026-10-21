# EMA Hourly Continuation — NFT/USDT P89_100

**Symbol:** NFT/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 149 |
| net_profit_factor | 0.2183 |
| net_win_rate | 0.2685 |
| gross_profit_factor | 0.5018 |
| gross_win_rate | 0.2752 |
| sharpe_ratio | -5.7462 |
| sortino_ratio | -1.0484 |
| max_drawdown | 0.7200 |
| cagr | -0.3960 |
| net_avg_win | 50.1415 |
| net_avg_loss | -84.2778 |
| avg_hold_time_bars | 7.0738 |
| exposure | 0.0479 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
