# EMA Hourly Continuation — NFT/USDT P12_26

**Symbol:** NFT/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 388 |
| net_profit_factor | 0.2885 |
| net_win_rate | 0.2500 |
| gross_profit_factor | 0.5466 |
| gross_win_rate | 0.2552 |
| sharpe_ratio | -9.5015 |
| sortino_ratio | -2.7984 |
| max_drawdown | 0.9692 |
| cagr | -0.7500 |
| net_avg_win | 40.5238 |
| net_avg_loss | -46.8153 |
| avg_hold_time_bars | 6.4794 |
| exposure | 0.1143 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
