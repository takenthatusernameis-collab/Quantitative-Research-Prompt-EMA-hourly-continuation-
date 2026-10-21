# EMA Hourly Continuation — NFT/USDT P20_26

**Symbol:** NFT/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 225 |
| net_profit_factor | 0.1788 |
| net_win_rate | 0.1867 |
| gross_profit_factor | 0.3646 |
| gross_win_rate | 0.1911 |
| sharpe_ratio | -8.2778 |
| sortino_ratio | -1.9015 |
| max_drawdown | 0.9095 |
| cagr | -0.6158 |
| net_avg_win | 47.1408 |
| net_avg_loss | -60.5168 |
| avg_hold_time_bars | 6.4400 |
| exposure | 0.0659 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
