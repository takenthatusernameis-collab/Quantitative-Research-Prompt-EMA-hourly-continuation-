# EMA Hourly Continuation — JTO/USDT P8_55

**Symbol:** JTO/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 672 |
| net_profit_factor | 0.7889 |
| net_win_rate | 0.4851 |
| gross_profit_factor | 0.9467 |
| gross_win_rate | 0.4851 |
| sharpe_ratio | -1.9760 |
| sortino_ratio | -0.7308 |
| max_drawdown | 0.6137 |
| cagr | -0.2875 |
| net_avg_win | 65.7118 |
| net_avg_loss | -78.4766 |
| avg_hold_time_bars | 16.1071 |
| exposure | 0.4920 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
