# EMA Hourly Continuation — DCR/USDT P21_34

**Symbol:** DCR/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1158 |
| net_profit_factor | 0.3616 |
| net_win_rate | 0.3981 |
| gross_profit_factor | 0.7976 |
| gross_win_rate | 0.4292 |
| sharpe_ratio | -11.3654 |
| sortino_ratio | -5.5038 |
| max_drawdown | 0.9992 |
| cagr | -0.9395 |
| net_avg_win | 12.2775 |
| net_avg_loss | -22.4555 |
| avg_hold_time_bars | 3.1157 |
| exposure | 0.1633 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
