# EMA Hourly Continuation — NFT/USDT P12_21

**Symbol:** NFT/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 304 |
| net_profit_factor | 0.2583 |
| net_win_rate | 0.2467 |
| gross_profit_factor | 0.5126 |
| gross_win_rate | 0.2500 |
| sharpe_ratio | -8.5271 |
| sortino_ratio | -2.2326 |
| max_drawdown | 0.9382 |
| cagr | -0.6699 |
| net_avg_win | 43.5561 |
| net_avg_loss | -55.2332 |
| avg_hold_time_bars | 5.8586 |
| exposure | 0.0810 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
