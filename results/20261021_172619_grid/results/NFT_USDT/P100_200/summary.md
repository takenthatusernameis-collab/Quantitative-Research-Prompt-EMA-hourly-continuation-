# EMA Hourly Continuation — NFT/USDT P100_200

**Symbol:** NFT/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 304 |
| net_profit_factor | 0.2865 |
| net_win_rate | 0.3092 |
| gross_profit_factor | 0.5150 |
| gross_win_rate | 0.3092 |
| sharpe_ratio | -6.8784 |
| sortino_ratio | -1.7479 |
| max_drawdown | 0.8743 |
| cagr | -0.5606 |
| net_avg_win | 37.3041 |
| net_avg_loss | -58.2803 |
| avg_hold_time_bars | 14.5789 |
| exposure | 0.2015 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
