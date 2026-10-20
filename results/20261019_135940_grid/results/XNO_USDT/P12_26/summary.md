# EMA Hourly Continuation — XNO/USDT P12_26

**Symbol:** XNO/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1554 |
| net_profit_factor | 0.3308 |
| net_win_rate | 0.3565 |
| gross_profit_factor | 0.7743 |
| gross_win_rate | 0.3835 |
| sharpe_ratio | -14.7346 |
| sortino_ratio | -8.2783 |
| max_drawdown | 1.0000 |
| cagr | -0.9852 |
| net_avg_win | 8.9210 |
| net_avg_loss | -14.9420 |
| avg_hold_time_bars | 2.7503 |
| exposure | 0.1943 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
