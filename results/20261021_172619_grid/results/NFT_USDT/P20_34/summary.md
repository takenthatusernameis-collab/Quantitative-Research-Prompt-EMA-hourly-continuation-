# EMA Hourly Continuation — NFT/USDT P20_34

**Symbol:** NFT/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 309 |
| net_profit_factor | 0.2452 |
| net_win_rate | 0.2460 |
| gross_profit_factor | 0.5055 |
| gross_win_rate | 0.2557 |
| sharpe_ratio | -8.6227 |
| sortino_ratio | -2.2801 |
| max_drawdown | 0.9401 |
| cagr | -0.6741 |
| net_avg_win | 40.1798 |
| net_avg_loss | -53.4552 |
| avg_hold_time_bars | 6.9482 |
| exposure | 0.0976 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
