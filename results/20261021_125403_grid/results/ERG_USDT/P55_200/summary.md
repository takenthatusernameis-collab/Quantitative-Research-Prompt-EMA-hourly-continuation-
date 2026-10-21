# EMA Hourly Continuation — ERG/USDT P55_200

**Symbol:** ERG/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 312 |
| net_profit_factor | 0.6947 |
| net_win_rate | 0.4679 |
| gross_profit_factor | 0.8742 |
| gross_win_rate | 0.4679 |
| sharpe_ratio | -1.9801 |
| sortino_ratio | -0.4976 |
| max_drawdown | 0.4404 |
| cagr | -0.2047 |
| net_avg_win | 68.1787 |
| net_avg_loss | -86.3173 |
| avg_hold_time_bars | 23.2436 |
| exposure | 0.3296 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
