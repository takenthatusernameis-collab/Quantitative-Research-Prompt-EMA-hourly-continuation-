# EMA Hourly Continuation — NFT/USDT P34_200

**Symbol:** NFT/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 701 |
| net_profit_factor | 0.2929 |
| net_win_rate | 0.2753 |
| gross_profit_factor | 0.6455 |
| gross_win_rate | 0.3124 |
| sharpe_ratio | -12.9514 |
| sortino_ratio | -5.1154 |
| max_drawdown | 0.9990 |
| cagr | -0.9356 |
| net_avg_win | 21.4395 |
| net_avg_loss | -27.8102 |
| avg_hold_time_bars | 16.8516 |
| exposure | 0.5370 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
