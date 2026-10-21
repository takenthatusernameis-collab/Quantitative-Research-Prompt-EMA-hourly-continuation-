# EMA Hourly Continuation — ZEC/USDT P21_26

**Symbol:** ZEC/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 126 |
| net_profit_factor | 0.7169 |
| net_win_rate | 0.4841 |
| gross_profit_factor | 0.9386 |
| gross_win_rate | 0.4841 |
| sharpe_ratio | -1.1667 |
| sortino_ratio | -0.1873 |
| max_drawdown | 0.2351 |
| cagr | -0.0827 |
| net_avg_win | 80.8779 |
| net_avg_loss | -105.8706 |
| avg_hold_time_bars | 5.0317 |
| exposure | 0.0288 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
