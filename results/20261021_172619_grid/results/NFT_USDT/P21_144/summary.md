# EMA Hourly Continuation — NFT/USDT P21_144

**Symbol:** NFT/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 443 |
| net_profit_factor | 0.4039 |
| net_win_rate | 0.3363 |
| gross_profit_factor | 0.6391 |
| gross_win_rate | 0.3386 |
| sharpe_ratio | -7.1806 |
| sortino_ratio | -2.1766 |
| max_drawdown | 0.9256 |
| cagr | -0.6409 |
| net_avg_win | 41.9954 |
| net_avg_loss | -52.6989 |
| avg_hold_time_bars | 22.3725 |
| exposure | 0.4505 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
