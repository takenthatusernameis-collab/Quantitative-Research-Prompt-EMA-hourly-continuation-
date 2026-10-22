# EMA Hourly Continuation — NFT/USDT P20_144

**Symbol:** NFT/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1020 |
| net_profit_factor | 0.3051 |
| net_win_rate | 0.2539 |
| gross_profit_factor | 0.6954 |
| gross_win_rate | 0.2843 |
| sharpe_ratio | -16.6551 |
| sortino_ratio | -7.9828 |
| max_drawdown | 1.0000 |
| cagr | -0.9868 |
| net_avg_win | 16.9537 |
| net_avg_loss | -18.9104 |
| avg_hold_time_bars | 10.6784 |
| exposure | 0.4951 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
