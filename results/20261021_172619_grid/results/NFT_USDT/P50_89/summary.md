# EMA Hourly Continuation — NFT/USDT P50_89

**Symbol:** NFT/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 325 |
| net_profit_factor | 0.3036 |
| net_win_rate | 0.3015 |
| gross_profit_factor | 0.6170 |
| gross_win_rate | 0.3046 |
| sharpe_ratio | -7.6363 |
| sortino_ratio | -2.0300 |
| max_drawdown | 0.9125 |
| cagr | -0.6197 |
| net_avg_win | 40.5613 |
| net_avg_loss | -57.6777 |
| avg_hold_time_bars | 9.1631 |
| exposure | 0.1354 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
