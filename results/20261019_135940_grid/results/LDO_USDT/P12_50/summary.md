# EMA Hourly Continuation — LDO/USDT P12_50

**Symbol:** LDO/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1118 |
| net_profit_factor | 0.4766 |
| net_win_rate | 0.4419 |
| gross_profit_factor | 0.7897 |
| gross_win_rate | 0.4535 |
| sharpe_ratio | -7.3852 |
| sortino_ratio | -3.4486 |
| max_drawdown | 0.9862 |
| cagr | -0.8181 |
| net_avg_win | 18.1763 |
| net_avg_loss | -30.1933 |
| avg_hold_time_bars | 6.5760 |
| exposure | 0.3342 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
