# EMA Hourly Continuation — CHZ/USDT P12_26

**Symbol:** CHZ/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 478 |
| net_profit_factor | 0.7143 |
| net_win_rate | 0.5063 |
| gross_profit_factor | 1.0157 |
| gross_win_rate | 0.5063 |
| sharpe_ratio | -2.2216 |
| sortino_ratio | -0.6990 |
| max_drawdown | 0.5852 |
| cagr | -0.2730 |
| net_avg_win | 56.9192 |
| net_avg_loss | -81.7151 |
| avg_hold_time_bars | 5.2782 |
| exposure | 0.1147 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
