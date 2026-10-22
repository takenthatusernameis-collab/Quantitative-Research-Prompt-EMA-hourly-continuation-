# EMA Hourly Continuation — ARB/USDT P21_34

**Symbol:** ARB/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1088 |
| net_profit_factor | 0.2902 |
| net_win_rate | 0.4357 |
| gross_profit_factor | 0.7559 |
| gross_win_rate | 0.4485 |
| sharpe_ratio | -9.9661 |
| sortino_ratio | -4.6425 |
| max_drawdown | 0.9975 |
| cagr | -0.9073 |
| net_avg_win | 8.6029 |
| net_avg_loss | -22.8865 |
| avg_hold_time_bars | 2.6011 |
| exposure | 0.1286 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
