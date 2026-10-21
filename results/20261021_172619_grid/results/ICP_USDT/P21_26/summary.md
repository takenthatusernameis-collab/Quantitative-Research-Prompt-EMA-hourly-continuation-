# EMA Hourly Continuation — ICP/USDT P21_26

**Symbol:** ICP/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 132 |
| net_profit_factor | 0.6191 |
| net_win_rate | 0.4697 |
| gross_profit_factor | 0.8782 |
| gross_win_rate | 0.4697 |
| sharpe_ratio | -1.6868 |
| sortino_ratio | -0.2776 |
| max_drawdown | 0.2931 |
| cagr | -0.1196 |
| net_avg_win | 71.7864 |
| net_avg_loss | -102.6935 |
| avg_hold_time_bars | 4.0530 |
| exposure | 0.0243 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
