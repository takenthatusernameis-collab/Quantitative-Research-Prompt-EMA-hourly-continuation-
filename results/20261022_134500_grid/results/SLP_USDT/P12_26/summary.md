# EMA Hourly Continuation — SLP/USDT P12_26

**Symbol:** SLP/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1551 |
| net_profit_factor | 0.3793 |
| net_win_rate | 0.3952 |
| gross_profit_factor | 0.8312 |
| gross_win_rate | 0.4178 |
| sharpe_ratio | -13.0139 |
| sortino_ratio | -7.3180 |
| max_drawdown | 0.9999 |
| cagr | -0.9739 |
| net_avg_win | 9.9686 |
| net_avg_loss | -17.1745 |
| avg_hold_time_bars | 3.0148 |
| exposure | 0.2125 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
