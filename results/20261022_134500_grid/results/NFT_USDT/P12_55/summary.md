# EMA Hourly Continuation — NFT/USDT P12_55

**Symbol:** NFT/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1508 |
| net_profit_factor | 0.2345 |
| net_win_rate | 0.2341 |
| gross_profit_factor | 0.6564 |
| gross_win_rate | 0.2878 |
| sharpe_ratio | -21.9854 |
| sortino_ratio | -13.0711 |
| max_drawdown | 1.0000 |
| cagr | -0.9993 |
| net_avg_win | 8.6798 |
| net_avg_loss | -11.3108 |
| avg_hold_time_bars | 5.8229 |
| exposure | 0.3991 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
