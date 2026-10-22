# EMA Hourly Continuation — NFT/USDT P8_26

**Symbol:** NFT/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 2112 |
| net_profit_factor | 0.1178 |
| net_win_rate | 0.1889 |
| gross_profit_factor | 0.4535 |
| gross_win_rate | 0.2538 |
| sharpe_ratio | -29.3905 |
| sortino_ratio | -21.4034 |
| max_drawdown | 1.0000 |
| cagr | -1.0000 |
| net_avg_win | 3.3457 |
| net_avg_loss | -6.6170 |
| avg_hold_time_bars | 3.0952 |
| exposure | 0.2971 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
