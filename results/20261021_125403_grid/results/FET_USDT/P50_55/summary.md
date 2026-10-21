# EMA Hourly Continuation — FET/USDT P50_55

**Symbol:** FET/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 72 |
| net_profit_factor | 0.3759 |
| net_win_rate | 0.3333 |
| gross_profit_factor | 0.4864 |
| gross_win_rate | 0.3333 |
| sharpe_ratio | -2.4191 |
| sortino_ratio | -0.2892 |
| max_drawdown | 0.2872 |
| cagr | -0.1261 |
| net_avg_win | 72.0866 |
| net_avg_loss | -95.8745 |
| avg_hold_time_bars | 7.4722 |
| exposure | 0.0245 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
