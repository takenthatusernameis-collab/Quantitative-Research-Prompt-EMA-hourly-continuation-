# EMA Hourly Continuation — NFT/USDT P12_20

**Symbol:** NFT/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 2054 |
| net_profit_factor | 0.0819 |
| net_win_rate | 0.1412 |
| gross_profit_factor | 0.5108 |
| gross_win_rate | 0.2313 |
| sharpe_ratio | -31.7075 |
| sortino_ratio | -24.1735 |
| max_drawdown | 1.0000 |
| cagr | -1.0000 |
| net_avg_win | 3.0747 |
| net_avg_loss | -6.1744 |
| avg_hold_time_bars | 2.1115 |
| exposure | 0.1971 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
