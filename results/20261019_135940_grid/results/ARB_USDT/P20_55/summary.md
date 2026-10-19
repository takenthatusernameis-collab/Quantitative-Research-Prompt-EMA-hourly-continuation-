# EMA Hourly Continuation — ARB/USDT P20_55

**Symbol:** ARB/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 915 |
| net_profit_factor | 0.4857 |
| net_win_rate | 0.4667 |
| gross_profit_factor | 0.8715 |
| gross_win_rate | 0.4732 |
| sharpe_ratio | -6.1128 |
| sortino_ratio | -2.5956 |
| max_drawdown | 0.9603 |
| cagr | -0.7209 |
| net_avg_win | 21.2235 |
| net_avg_loss | -38.2312 |
| avg_hold_time_bars | 5.6175 |
| exposure | 0.2336 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
