# EMA Hourly Continuation — KAS/USDT P20_55

**Symbol:** KAS/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1030 |
| net_profit_factor | 0.4263 |
| net_win_rate | 0.4738 |
| gross_profit_factor | 0.8193 |
| gross_win_rate | 0.4854 |
| sharpe_ratio | -6.8066 |
| sortino_ratio | -3.0690 |
| max_drawdown | 0.9786 |
| cagr | -0.7800 |
| net_avg_win | 14.8885 |
| net_avg_loss | -31.4437 |
| avg_hold_time_bars | 4.7680 |
| exposure | 0.2232 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
