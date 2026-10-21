# EMA Hourly Continuation — YGG/USDT P21_34

**Symbol:** YGG/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 389 |
| net_profit_factor | 0.6259 |
| net_win_rate | 0.4550 |
| gross_profit_factor | 0.8644 |
| gross_win_rate | 0.4550 |
| sharpe_ratio | -3.2226 |
| sortino_ratio | -0.9047 |
| max_drawdown | 0.6712 |
| cagr | -0.3401 |
| net_avg_win | 61.4045 |
| net_avg_loss | -81.9057 |
| avg_hold_time_bars | 4.4833 |
| exposure | 0.0789 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
