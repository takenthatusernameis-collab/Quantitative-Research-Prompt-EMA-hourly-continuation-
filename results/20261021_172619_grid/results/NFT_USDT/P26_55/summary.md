# EMA Hourly Continuation — NFT/USDT P26_55

**Symbol:** NFT/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 401 |
| net_profit_factor | 0.2972 |
| net_win_rate | 0.2918 |
| gross_profit_factor | 0.5704 |
| gross_win_rate | 0.2968 |
| sharpe_ratio | -8.7185 |
| sortino_ratio | -2.5822 |
| max_drawdown | 0.9570 |
| cagr | -0.7105 |
| net_avg_win | 34.5433 |
| net_avg_loss | -47.8761 |
| avg_hold_time_bars | 9.1820 |
| exposure | 0.1674 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
