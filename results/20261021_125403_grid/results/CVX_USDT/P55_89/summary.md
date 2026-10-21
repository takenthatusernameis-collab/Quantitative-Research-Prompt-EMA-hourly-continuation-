# EMA Hourly Continuation — CVX/USDT P55_89

**Symbol:** CVX/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 340 |
| net_profit_factor | 0.8321 |
| net_win_rate | 0.5265 |
| gross_profit_factor | 1.1138 |
| gross_win_rate | 0.5265 |
| sharpe_ratio | -1.0811 |
| sortino_ratio | -0.2875 |
| max_drawdown | 0.3146 |
| cagr | -0.1250 |
| net_avg_win | 78.8723 |
| net_avg_loss | -105.3838 |
| avg_hold_time_bars | 7.1765 |
| exposure | 0.1109 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
