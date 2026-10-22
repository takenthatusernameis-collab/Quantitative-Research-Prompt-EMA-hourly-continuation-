# EMA Hourly Continuation — NFT/USDT P20_89

**Symbol:** NFT/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1262 |
| net_profit_factor | 0.2859 |
| net_win_rate | 0.2425 |
| gross_profit_factor | 0.7109 |
| gross_win_rate | 0.2868 |
| sharpe_ratio | -19.5299 |
| sortino_ratio | -10.5733 |
| max_drawdown | 1.0000 |
| cagr | -0.9971 |
| net_avg_win | 13.0855 |
| net_avg_loss | -14.6487 |
| avg_hold_time_bars | 6.9208 |
| exposure | 0.3970 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
