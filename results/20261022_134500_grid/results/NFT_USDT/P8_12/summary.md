# EMA Hourly Continuation — NFT/USDT P8_12

**Symbol:** NFT/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 2421 |
| net_profit_factor | 0.0525 |
| net_win_rate | 0.1219 |
| gross_profit_factor | 0.3617 |
| gross_win_rate | 0.2251 |
| sharpe_ratio | -35.9306 |
| sortino_ratio | -30.1907 |
| max_drawdown | 1.0000 |
| cagr | -1.0000 |
| net_avg_win | 1.8800 |
| net_avg_loss | -4.9645 |
| avg_hold_time_bars | 1.6543 |
| exposure | 0.1820 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
