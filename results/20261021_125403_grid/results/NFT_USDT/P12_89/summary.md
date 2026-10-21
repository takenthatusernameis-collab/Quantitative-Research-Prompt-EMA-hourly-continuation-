# EMA Hourly Continuation — NFT/USDT P12_89

**Symbol:** NFT/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 536 |
| net_profit_factor | 0.4342 |
| net_win_rate | 0.3507 |
| gross_profit_factor | 0.7145 |
| gross_win_rate | 0.3507 |
| sharpe_ratio | -7.8636 |
| sortino_ratio | -2.6286 |
| max_drawdown | 0.9572 |
| cagr | -0.7117 |
| net_avg_win | 39.0203 |
| net_avg_loss | -48.5514 |
| avg_hold_time_bars | 17.3843 |
| exposure | 0.4235 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
