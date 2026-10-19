# EMA Hourly Continuation — NFT/USDT P89_144

**Symbol:** NFT/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 943 |
| net_profit_factor | 0.1858 |
| net_win_rate | 0.2078 |
| gross_profit_factor | 0.5883 |
| gross_win_rate | 0.2556 |
| sharpe_ratio | -18.3649 |
| sortino_ratio | -8.9198 |
| max_drawdown | 1.0000 |
| cagr | -0.9928 |
| net_avg_win | 11.6446 |
| net_avg_loss | -16.4422 |
| avg_hold_time_bars | 4.2778 |
| exposure | 0.1834 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
