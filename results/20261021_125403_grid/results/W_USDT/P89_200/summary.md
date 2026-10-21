# EMA Hourly Continuation — W/USDT P89_200

**Symbol:** W/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 272 |
| net_profit_factor | 1.0089 |
| net_win_rate | 0.5551 |
| gross_profit_factor | 1.2353 |
| gross_win_rate | 0.5551 |
| sharpe_ratio | 0.0964 |
| sortino_ratio | 0.0231 |
| max_drawdown | 0.1166 |
| cagr | 0.0046 |
| net_avg_win | 87.9025 |
| net_avg_loss | -108.7327 |
| avg_hold_time_bars | 15.9853 |
| exposure | 0.1976 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
