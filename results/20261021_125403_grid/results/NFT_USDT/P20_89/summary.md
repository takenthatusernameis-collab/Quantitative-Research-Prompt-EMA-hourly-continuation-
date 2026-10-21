# EMA Hourly Continuation — NFT/USDT P20_89

**Symbol:** NFT/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 468 |
| net_profit_factor | 0.4136 |
| net_win_rate | 0.3632 |
| gross_profit_factor | 0.7093 |
| gross_win_rate | 0.3654 |
| sharpe_ratio | -7.1978 |
| sortino_ratio | -2.2574 |
| max_drawdown | 0.9326 |
| cagr | -0.6549 |
| net_avg_win | 38.6232 |
| net_avg_loss | -53.2708 |
| avg_hold_time_bars | 16.7286 |
| exposure | 0.3559 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
