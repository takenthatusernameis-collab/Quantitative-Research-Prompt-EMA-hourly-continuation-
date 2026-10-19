# EMA Hourly Continuation — NFT/USDT P21_55

**Symbol:** NFT/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1532 |
| net_profit_factor | 0.1890 |
| net_win_rate | 0.2121 |
| gross_profit_factor | 0.5715 |
| gross_win_rate | 0.2696 |
| sharpe_ratio | -23.4818 |
| sortino_ratio | -14.3747 |
| max_drawdown | 1.0000 |
| cagr | -0.9997 |
| net_avg_win | 7.1684 |
| net_avg_loss | -10.2152 |
| avg_hold_time_bars | 4.1214 |
| exposure | 0.2870 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
