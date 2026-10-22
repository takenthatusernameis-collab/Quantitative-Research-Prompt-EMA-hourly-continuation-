# EMA Hourly Continuation — YGG/USDT P12_26

**Symbol:** YGG/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 578 |
| net_profit_factor | 0.7344 |
| net_win_rate | 0.4862 |
| gross_profit_factor | 1.0034 |
| gross_win_rate | 0.4896 |
| sharpe_ratio | -2.8077 |
| sortino_ratio | -0.9651 |
| max_drawdown | 0.6914 |
| cagr | -0.3572 |
| net_avg_win | 66.1439 |
| net_avg_loss | -85.2075 |
| avg_hold_time_bars | 4.8426 |
| exposure | 0.1267 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
