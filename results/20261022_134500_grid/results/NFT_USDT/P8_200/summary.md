# EMA Hourly Continuation — NFT/USDT P8_200

**Symbol:** NFT/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 789 |
| net_profit_factor | 0.3178 |
| net_win_rate | 0.2902 |
| gross_profit_factor | 0.7040 |
| gross_win_rate | 0.3207 |
| sharpe_ratio | -13.0849 |
| sortino_ratio | -5.3951 |
| max_drawdown | 0.9993 |
| cagr | -0.9456 |
| net_avg_win | 20.3293 |
| net_avg_loss | -26.1585 |
| avg_hold_time_bars | 20.0152 |
| exposure | 0.7178 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
