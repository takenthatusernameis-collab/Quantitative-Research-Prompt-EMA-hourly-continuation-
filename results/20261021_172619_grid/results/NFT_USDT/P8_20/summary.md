# EMA Hourly Continuation — NFT/USDT P8_20

**Symbol:** NFT/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 434 |
| net_profit_factor | 0.3048 |
| net_win_rate | 0.2811 |
| gross_profit_factor | 0.5946 |
| gross_win_rate | 0.2857 |
| sharpe_ratio | -9.3773 |
| sortino_ratio | -2.8976 |
| max_drawdown | 0.9717 |
| cagr | -0.7580 |
| net_avg_win | 34.9139 |
| net_avg_loss | -44.7950 |
| avg_hold_time_bars | 5.9931 |
| exposure | 0.1182 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
