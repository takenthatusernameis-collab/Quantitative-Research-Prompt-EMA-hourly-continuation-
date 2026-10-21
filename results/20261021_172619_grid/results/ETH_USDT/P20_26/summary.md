# EMA Hourly Continuation — ETH/USDT P20_26

**Symbol:** ETH/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 143 |
| net_profit_factor | 0.6076 |
| net_win_rate | 0.5035 |
| gross_profit_factor | 1.0022 |
| gross_win_rate | 0.5035 |
| sharpe_ratio | -1.7794 |
| sortino_ratio | -0.3066 |
| max_drawdown | 0.3073 |
| cagr | -0.1303 |
| net_avg_win | 63.6032 |
| net_avg_loss | -106.1571 |
| avg_hold_time_bars | 5.5524 |
| exposure | 0.0361 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
