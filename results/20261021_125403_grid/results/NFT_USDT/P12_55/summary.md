# EMA Hourly Continuation — NFT/USDT P12_55

**Symbol:** NFT/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 568 |
| net_profit_factor | 0.3867 |
| net_win_rate | 0.3327 |
| gross_profit_factor | 0.6844 |
| gross_win_rate | 0.3363 |
| sharpe_ratio | -9.0342 |
| sortino_ratio | -3.1342 |
| max_drawdown | 0.9771 |
| cagr | -0.7762 |
| net_avg_win | 32.5863 |
| net_avg_loss | -42.0208 |
| avg_hold_time_bars | 12.5335 |
| exposure | 0.3236 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
