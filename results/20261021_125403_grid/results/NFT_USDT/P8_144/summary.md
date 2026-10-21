# EMA Hourly Continuation — NFT/USDT P8_144

**Symbol:** NFT/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 490 |
| net_profit_factor | 0.4418 |
| net_win_rate | 0.3510 |
| gross_profit_factor | 0.6773 |
| gross_win_rate | 0.3531 |
| sharpe_ratio | -6.9954 |
| sortino_ratio | -2.2188 |
| max_drawdown | 0.9293 |
| cagr | -0.6481 |
| net_avg_win | 42.6752 |
| net_avg_loss | -52.2464 |
| avg_hold_time_bars | 26.6306 |
| exposure | 0.5931 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
