# EMA Hourly Continuation — NFT/USDT P89_200

**Symbol:** NFT/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 808 |
| net_profit_factor | 0.1881 |
| net_win_rate | 0.2067 |
| gross_profit_factor | 0.4843 |
| gross_win_rate | 0.2500 |
| sharpe_ratio | -16.2140 |
| sortino_ratio | -7.0921 |
| max_drawdown | 0.9999 |
| cagr | -0.9788 |
| net_avg_win | 13.8696 |
| net_avg_loss | -19.2131 |
| avg_hold_time_bars | 7.0545 |
| exposure | 0.2591 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
