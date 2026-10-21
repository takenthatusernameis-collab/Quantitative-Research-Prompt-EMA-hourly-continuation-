# EMA Hourly Continuation — NYM/USDT P20_21

**Symbol:** NYM/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 194 |
| net_profit_factor | 0.2545 |
| net_win_rate | 0.3557 |
| gross_profit_factor | 0.5408 |
| gross_win_rate | 0.3608 |
| sharpe_ratio | -5.0139 |
| sortino_ratio | -1.0102 |
| max_drawdown | 0.7075 |
| cagr | -0.3871 |
| net_avg_win | 35.0100 |
| net_avg_loss | -75.9254 |
| avg_hold_time_bars | 8.9742 |
| exposure | 0.0791 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
