# EMA Hourly Continuation — NFT/USDT P8_20

**Symbol:** NFT/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 2269 |
| net_profit_factor | 0.0973 |
| net_win_rate | 0.1714 |
| gross_profit_factor | 0.4270 |
| gross_win_rate | 0.2437 |
| sharpe_ratio | -31.7671 |
| sortino_ratio | -24.4409 |
| max_drawdown | 1.0000 |
| cagr | -1.0000 |
| net_avg_win | 2.7707 |
| net_avg_loss | -5.8924 |
| avg_hold_time_bars | 2.4350 |
| exposure | 0.2511 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
