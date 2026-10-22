# EMA Hourly Continuation — CRO/USDT P20_34

**Symbol:** CRO/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1226 |
| net_profit_factor | 0.2285 |
| net_win_rate | 0.3581 |
| gross_profit_factor | 0.8649 |
| gross_win_rate | 0.4209 |
| sharpe_ratio | -14.4766 |
| sortino_ratio | -7.3702 |
| max_drawdown | 0.9999 |
| cagr | -0.9792 |
| net_avg_win | 6.7454 |
| net_avg_loss | -16.4684 |
| avg_hold_time_bars | 2.6949 |
| exposure | 0.1502 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
