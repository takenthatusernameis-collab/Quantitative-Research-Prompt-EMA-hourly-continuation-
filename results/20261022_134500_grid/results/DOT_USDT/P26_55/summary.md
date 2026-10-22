# EMA Hourly Continuation — DOT/USDT P26_55

**Symbol:** DOT/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 869 |
| net_profit_factor | 0.4496 |
| net_win_rate | 0.4603 |
| gross_profit_factor | 0.8852 |
| gross_win_rate | 0.4672 |
| sharpe_ratio | -7.2190 |
| sortino_ratio | -2.9750 |
| max_drawdown | 0.9785 |
| cagr | -0.7807 |
| net_avg_win | 19.9696 |
| net_avg_loss | -37.8816 |
| avg_hold_time_bars | 4.3349 |
| exposure | 0.1712 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
